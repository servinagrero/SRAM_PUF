#!/usr/bin/env python3
#
# TODO: Store the final results in a database (mongodb)
# TODO: Create combinations only for the same region of memory

import re
from itertools import combinations
from pathlib import Path
import argparse
import datetime

dump_re = r'.*-(\d{2}-\d{2}-\d{4})-(.{4})-(\d+)$'

ap = argparse.ArgumentParser()
ap.add_argument("-d", "--dir", required=False,
                help="directory with the binary files.")
ap.add_argument("-s", "--store", required=False, nargs='?',
                const="results.csv", help="store the results in a csv file")

MSG_LENGTH = 1024


def file_is_valid(filename):
    '''Checks if the file lenght is equal to MSG_LENGTH.'''
    with open(filename, "rb") as f:
        return True if len(f.read()) == MSG_LENGTH else False


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


def extract_data(files_list):
    final_list = []
    for (f1, f2) in files_list:
        msg1 = open(f1, "rb").read()
        msg2 = open(f2, "rb").read()
        final_list.append((msg1, msg2))
    return final_list


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
