#!/usr/bin/python
#
# Program to store and retrieve memory dumps into a mongo database

import pymongo
import serial
import usb.core
import usb.util

import dump

STM32_VENDOR = 0x0483
SERIAL_DEV = '/dev/ttyACM'
BAUD_RATE = 19600

client = pymongo.MongoClient("mongodb://localhost:27017/")
database = client['memory_dumps']
db_dumps = database['dumps']

c = 0
ser = None
dev = usb.core.find(idVendor=STM32_VENDOR)

while ser is None:
    try:
        ser = serial.Serial(SERIAL_DEV+str(c), BAUD_RATE)
    except serial.SerialException:
        c += 1

print(f'Device {dev.serial_number} in port {ser.port}')

while True:
    mem_address = ser.readline().decode("utf-8")
    raw_data = ser.readline().decode("utf-8")

    mem_address = mem_address[:-1]
    raw_data = raw_data.split(' ')[:-2]

    dump_data = dump.Dump(dev.serial_number,
                          raw_data,
                          mem_address)

# dump_data = dump.Dump(dev.serial_number,
#                       bytes([int(c) for c in raw_data]),
#                       mem_address)

    result = db_dumps.insert_one(dump_data.__dict__())
    print(f'{dev.serial_number} [{mem_address}] -> ID {result.inserted_id}')
