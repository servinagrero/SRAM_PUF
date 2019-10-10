#!/usr/bin/python
#
# Program to store and retrieve memory dumps into a mongo database

import pymongo
import serial
import usb.core
import usb.util

import dump

# STM32_VENDOR = 0x0483
STM32_VENDOR = 0x067b
SERIAL_DEV = '/dev/ttyUSB'
BAUD_RATE = 350000

client = pymongo.MongoClient("mongodb://localhost:27017/")
database = client['memory_dumps']
db_dumps = database['dumps']

ser = None


def bind_devices():
    C = 0
    global ser, dev
    while ser is None:
        try:
            ser = serial.Serial(SERIAL_DEV+str(C), BAUD_RATE)
        except serial.SerialException:
            C = 1 if C == 0 else 0

    print(f'[   CONNECTED] Board in port {ser.port}')


while True:
    bind_devices()

    serial_num = ser.readline().decode("utf-8")[:-1]

    for i in range(0, 16):
        mem_address = ser.readline().decode("utf-8")
        temp = ser.readline().decode("utf-8")
        raw_data = ser.readline().decode("utf-8")

        temp = temp[:-1]
        mem_address = mem_address[:-1]
        raw_data = raw_data.split(' ')[:-1]

        dump_data = dump.Dump(serial_num,
                              raw_data,
                              mem_address,
                              temp)

        result = db_dumps.insert_one(dump_data.__dict__())
        print(f'{serial_num} [{mem_address}] at {dump_data.timestamp}')

    ser.close()
    print(f'[DISCONNECTED] Board in port {ser.port}')
    ser = None

    selection = input("Press a key when the board is reconnected. q to exit. ")
    if selection == 'q':
        exit(1)
