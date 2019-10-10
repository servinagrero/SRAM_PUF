#!/usr/bin/env python3
#
# Class to store memory dumps from the boards

from itertools import combinations
from pathlib import Path
from datetime import datetime

MSG_LENGTH = 1024


class Dump():

    def __init__(self, board_id, data, mem_pos, temp,
                 length=None, fd=None, timestamp=None):
        self.board_id = board_id
        self.temp = temp
        self.timestamp = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
        self.mem_pos = mem_pos
        self.fd = fd
        if fd is not None:
            with open(fd, "rb") as f_data:
                self.data = f_data.read()
        else:
            self.data = data
        self.length = len(data) if length is None else length

    def __eq__(self, other):
        if self.length != other.length:
            raise ValueError("The length of the dumps is not the same")

        for i in range(0, self.length):
            if self.data[i] != other.data[i]:
                return False
        else:
            return True

    def __and__(self, other):
        diff = 0
        for i in range(0, self.length):
            if self.data[i] != other.data[i]:
                diff += 1
        return diff/self.length

    def __dict__(self):
        return {'board_id': self.board_id,
                'mem_pos': self.mem_pos,
                'temp': self.temp,
                'lenght': self.length,
                'timestamp': self.timestamp,
                'data': self.data
                }


def calc_diff(dump1, dump2):
    '''Calculate the difference between two dumps of data'''
    diff = 0
    for i in range(0, dump1.length):
        if dump1.data[i] != dump2.data[i]:
            diff += 1
    return diff / dump1.lenght


def compare_files(file1, file2):
    '''Checks if two files differ and by how much.'''
    differ = 0
    for i in range(0, MSG_LENGTH):
        if file1[i] != file2[i]:
            differ += 1
    return (differ / MSG_LENGTH) * 100


def create_files_combinations(data_dir):
    path = Path(data_dir)
    files = [f.as_posix() for f in path.iterdir()
             if f.is_file() and file_is_valid(f.as_posix())]
    return list(combinations(files, 2))


def filter_results(data_list, num=20):
    final_list = []
    for i, (f1, f2, d) in enumerate(data_list):
        if d < num:
            final_list.append((f1, f2, d))
    return final_list


if __name__ == '__main__':
    args = vars(ap.parse_args())

    if not args["dir"]:
        ap.print_help()
        exit(1)

    if args["store"]:
        csv_file = open(args["store"], "w")

    results = []
    data_files = create_files_combinations(args["dir"])
    msg_list = extract_data(data_files)
    for c, (msg1, msg2) in enumerate(msg_list):
        d = compare_files(msg1, msg2)
        results.append((data_files[c][0], data_files[c][1], d))

    results = sorted(results, key=lambda tup: tup[2])
    for c, (f1, f2, d) in enumerate(results):
        match_f1 = re.match(dump_re, f1)
        match_f2 = re.match(dump_re, f2)
        print(f'Files {f1} and {f2} differ by {d} %')
        if args["store"]:
            csv_file.write(f'0x2000{match_f1.group(2)},0x2000{match_f2.group(2)},{d:2.2f}\n')

    good_list = filter_results(results)
    if args["store"]:
        csv_file.close()
