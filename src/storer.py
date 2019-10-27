#!/usr/bin/python
#
# Program to store and retrieve memory dumps into a mongo database

import pymongo
import serial

import dump

SERIAL_DEV = '/dev/ttyUSB'
BAUD_RATE = 350000

CHUNK_NUM = 32  # Number of memory chunks to store

# Initialization of the mongo database
client = pymongo.MongoClient("mongodb://localhost:27017/")
database = client['memory_dumps']
db_dumps = database['dumps']

ser = None


def bind_devices():
    '''Wait for the board to be available to connect.'''
    C = 0
    global ser, dev
    while ser is None:
        try:
            ser = serial.Serial(SERIAL_DEV+str(C), BAUD_RATE)
        except serial.SerialException:
            C = 1 if C == 0 else 0

    print(f'[   CONNECTED] Board in port {ser.port}')
    ser.read_all()


while True:
    bind_devices()

    serial_num = ser.readline().decode("utf-8")[:-1]
    temp_cal_30 = int(ser.readline().decode("utf-8")[:-1])
    temp_cal_110 = int(ser.readline().decode("utf-8")[:-1])
    vrefint_cal = int(ser.readline().decode("utf-8")[:-1])

    for i in range(0, CHUNK_NUM):
        mem_address = ser.readline().decode("utf-8")[:-1]
        vdd_raw = int(ser.readline().decode("utf-8")[:-1])
        temp_raw = int(ser.readline().decode("utf-8")[:-1])
        raw_data = ser.readline().decode("utf-8")

        raw_data = [int(b) for b in raw_data.split(' ')[:-1]]

        # According to the datasheet, VDD is calculated
        # VDD = 3.3 * VREFINT_CAL / VREFINT_DATA
        vdd = (3300 * vrefint_cal / vdd_raw) * 0.001

        # According to the datasheet, Tint is calculated
        # We need the calibration values at 30 and 100 degrees
        # temp = ((110 - 30)/ (Ts_cal_110 - Ts_cal_30))
        #        * (Ts_data - Ts_cal_30) + 30.0

        temp = ((110 - 30) / (temp_cal_110 - temp_cal_30)) \
            * (temp_raw - temp_cal_30) + 30.0

        dump_data = dump.Dump(serial_num, raw_data,
                              mem_address,
                              temp, vdd,
                              temp_cal_30, temp_cal_110, vrefint_cal)

        result = db_dumps.insert_one(dump_data.__dict__())
        print(f'{serial_num} [{mem_address}] at {dump_data.timestamp}')
        print(f'Temp: {temp:.6f} C, Vdd: {vdd:.8f} V\n')

    ser.close()
    print(f'[DISCONNECTED] Board in port {ser.port}')
    ser = None

    selection = input("Press a key when the board is reconnected. q to exit. ")
    if selection == 'q':
        exit(1)
