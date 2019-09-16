#!/usr/bin/env python3

import sys
# import argparse

# ap = argparse.ArgumentParser(description="Small script to compare two binary files")
# ap.add_argument("-f", "--file", required=True, help="Path to the first file.")
# args = vars(ap.parse_args())

# TODO: Given a directory with binary files, check all files and permutations
MSG_LENGTH = 1024


def file_is_valid(f):
    '''Checks if the file lenght is equal to MSG_LENGTH.'''
    return True if len(f) == 1024 else False


def compare_files(file1, file2):
    '''Checks if two files differ and by how much.'''
    differ = 0
    for i in range(0, MSG_LENGTH):
        if file1[i] != file2[i]:
            differ += 1
    return (differ / MSG_LENGTH) * 100


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Two files to compare must be provided")
        exit(1)
    else:
        file1 = open(sys.argv[1], "rb").read()
        file2 = open(sys.argv[2], "rb").read()
        if not file_is_valid(file1) or not file_is_valid(file2):
            print("Files must be 1024 bytes long.")
            exit(1)
        else:
            diff = compare_files(file1, file2)
            print(f'Difference between files is {diff:2.2f}%')
