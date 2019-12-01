#!/usr/bin/env python

# from pathlib import Path

try:
    import pymongo
    NOT_MONGO = False
except ImportError:
    NOT_MONGO = True

import sys
import serial
import serial.tools.list_ports
import argparse
from threading import Thread
import dump
import csv

BAUD_RATE = 350000
MONGO_URL = "mongodb://localhost:27017/"
boards_serials = []
args = None


CSV_FD = open('database.csv', 'w+')
fields = [
    "board_id", "mem_pos",
    "temp", "vdd", "temp_cal_30", "temp_cal_110", "vrefint_cal",
    "length", "timestamp", "data"
]

csvw = csv.DictWriter(CSV_FD, delimiter=',', fieldnames=fields,
                      quotechar='"', quoting=csv.QUOTE_MINIMAL)
csvw.writeheader()


# Look for open ports
def connect_boards():
    '''Connect to all open ports available'''
    if sys.platform.startswith('win'):
        ports_paths = list(serial.tools.list_ports.grep('.*COM.*'))
    elif sys.platform.startswith('linux'):
        # dev_dir = Path('/dev')
        # ports_paths = list(dev_dir.glob('ttyUSB*'))
        ports_paths = list(serial.tools.list_ports.grep('.*(USB|ACM).*'))

    print(f'Number of open ports: {len(ports_paths)}')

    boards = []
    # Bind devices on open ports
    for port in ports_paths:
        ser = serial.Serial(str(port[0]), BAUD_RATE)
        boards.append(ser)
        print(f'[CONNECTED   ] Board in port {port.device}')

    return boards


def store_data(data, csv):
    '''Store the data in a csv or in the mongo database'''
    if csv or NOT_MONGO:
        csvw.writerow(data)
        if args['verbose'] or args['more_verbose']:
            print(f'Dump {data["board_id"]} written to database.csv')
    else:
        mongo_client = pymongo.MongoClient(MONGO_URL)
        database = mongo_client['thesis']
        db = database['dumps']

        result = db.insert_one(data)
        if args['verbose'] or args['more_verbose']:
            print(f'Dump {result.inserted_id} written to database\n')


# Read data from the devices
def read_data(serial):
    '''
    Read data from one serial port and store it into the database
    We need one mongo client per connection
    '''
    # data = {}
    # Extract metadata

    serial_num = serial.readline().decode("utf-8")[:-1]
    temp_cal_30 = int(serial.readline().decode("utf-8"))
    temp_cal_110 = int(serial.readline().decode("utf-8"))
    vrefint_cal = int(serial.readline().decode("utf-8"))

    for i in range(args['size']):

        mem_address = serial.readline().decode("utf-8")[:-1]
        vdd_raw = int(serial.readline().decode("utf-8")[:-1])
        temp_raw = int(serial.readline().decode("utf-8")[:-1])
        raw_data = serial.readline().decode("utf-8")

        raw_data = [int(b) for b in raw_data.split(' ')[:-1]]

        # According to the datasheet, VDD is calculated
        # VDD = 3.3 * VREFINT_CAL / VREFINT_DATA
        if vrefint_cal == 0:
            vdd = vdd_raw
        else:
            vdd = (3300 * vrefint_cal / vdd_raw) * 0.001

        # According to the datasheet, Tint is calculated
        # We need the calibration values at 30 and 100 degrees
        # temp = ((110 - 30)/ (ts_cal_110 - ts_cal_30))
        #     * (ts_data - ts_cal_30) + 30.0

        if temp_cal_30 == 0 or temp_cal_110 == 0:
            temp = temp_raw
        else:
            temp = ((110 - 30) / (temp_cal_110 - temp_cal_30)) \
                * (temp_raw - temp_cal_30) + 30.0

        # Extract the memory data
        dump_data = dump.Dump(serial_num, raw_data,
                              mem_address,
                              temp, vdd,
                              temp_cal_30, temp_cal_110, vrefint_cal)

        if args['more_verbose']:
            print(f'{serial_num} [{mem_address}] at {dump_data.timestamp}')
            print(f'Temp: {temp:.6f} C, Vdd: {vdd:.8f} V')

        store_data(dump_data.__dict__, args['csv'])
    else:
        # Disconnect the serial port
        print(f'[DISCONNECTED] Board on port {serial.port}')
        serial.close()


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument("-v", required=False, dest='verbose',
                    action='store_true', help="Verbose option")
    ap.add_argument("-vv", required=False, dest='more_verbose',
                    action='store_true', help="More verbose option")
    ap.add_argument("-c", required=False, dest='continuous',
                    action='store_true', help="Continuous mode")
    ap.add_argument("-s", "--size", nargs='?', default=64, type=int,
                    help="Number of chunks to read per board")
    ap.add_argument("--csv", required=False, action='store_true',
                    help="Store dumps in database.csv")
    args = vars(ap.parse_args())

    if args['continuous']:
        num_samples = 1  # Number of samples taken

        while True:
            boards_serials = connect_boards()
            threads = []

            for board in boards_serials:
                th = Thread(target=read_data, args=(board,))
                threads.append(th)

            for t in threads:
                t.start()

            for t in threads:
                t.join()

            print(f'Sample number {num_samples}\n')

            c = input('Enter when the boards are disconnected. q to exit ')
            if c == 'q':
                CSV_FD.close()
                break
            else:
                num_samples += 1

    else:
        boards_serials = connect_boards()
        threads = []

        for board in boards_serials:
            th = Thread(target=read_data, args=(board,))
            threads.append(th)

        for t in threads:
            t.start()

        for t in threads:
            t.join()

        CSV_FD.close()
        exit(1)
