#!/usr/bin/env python3

import sys
from itertools import combinations
from pathlib import Path
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-f", "--files", required=False,
                nargs='+', help="Files to compare.")
ap.add_argument("-d", "--dir", required=False,
                help="Directory with the binary files.")

# TODO: Given a directory with binary files, check all files and permutations
MSG_LENGTH = 1024


def file_is_valid(filename):
    '''Checks if the file lenght is equal to MSG_LENGTH.'''
    with open(filename, "rb") as f:
        return True if len(f.read()) == 1024 else False


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


if __name__ == '__main__':
    args = vars(ap.parse_args())

    if not args["dir"] and not args["files"]:
        ap.print_help()
        exit(1)

    if args["dir"] and not args["files"]:
        results = []
        data_files = create_files_combinations(args["dir"])
        msg_list = extract_data(data_files)
        for c, (msg1, msg2) in enumerate(msg_list):
            d = compare_files(msg1, msg2)
            results.append((data_files[c][0], data_files[c][1], d))

        results = sorted(results, key=lambda tup: tup[2])
        for (f1, f2, d) in results:
            print(f'Files {f1} and {f2} differ by {d} %')

    # TODO: Fix this function
    if args["files"] and not args["dir"]:
        print(args["files"])
        data_files = create_files_combinations(args["files"])
        msg_list = extract_data(data_files)
        for c, (msg1, msg2) in enumerate(msg_list):
            d = compare_files(msg1, msg2)
            print(f'Files {data_files[c][0]} and {data_files[c][1]} differ by {d} %')

    # file_combinations = combinations(file_list, 2)
    # file1 = open(sys.argv[1], "rb").read()
    # file2 = open(sys.argv[2], "rb").read()
    # if not file_is_valid(file1) or not file_is_valid(file2):
    #     print("Files must be 1024 bytes long.")
    #     exit(1)
    # else:
    #     diff = compare_files(file1, file2)
    #     print(f'Difference between files is {diff:2.2f}%')
