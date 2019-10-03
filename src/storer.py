#!/usr/bin/python
#
# Program to store and retrieve memory dumps into a mongo database

import sys
import argparse
from pathlib import Path
import re

import pymongo
import usb.core
import usb.util

dump_re = r'.*-(\d{2}-\d{2}-\d{4})-(.{4})-(\d+)$'

client = pymongo.MongoClient("mongodb://localhost:27017/")

database = client['memory_dumps']
db_dumps = database['dumps']

path = Path(sys.argv[1])
data_files = [f.as_posix() for f in path.iterdir() if f.is_file()]

for in_file in data_files:
    match = re.match(dump_re, in_file)
    with open(in_file, "rb") as f:
        dump_data = {
                'board_id': 'UÿkHHSB9',
                'date': match.group(1),
                'mem_dump': f.read(),
                'mem_position': '0x2000' + match.group(2),
                }
        result = db_dumps.insert_one(dump_data)
        print(f'{"0x2000"+match.group(2)} -> ID {result.inserted_id}')
