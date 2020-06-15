#!/usr/bin/python

import pandas as pd

from pathlib import Path
from itertools import combinations

CHUNK_SIZE = 4096  # Size of each sample


def hamming(v1, v2):
    '''Hamming distance between two vectors'''
    return sum(map(int.__ne__, v1, v2))


def calculate_uniqueness(bType):
    '''
    Calculate the uniqueness for all pair of boards.

    Uniqueness is calculated by grouping boards in pairs and obtaining the hamming distance between one reference sample of each board from the same region.
    '''

    out_f = open(f'../data/processed/uniqueness_{bType}', "w")
    out_f.write('Board_Ref,Board,Mem_pos,Uniqueness\n')

    files = Path(f'../data/raw/{bType}')

    boards = pd.read_csv("../data/interim/boards_{bType}.csv")
    boards = boards.columns.to_list()
    boards_combs = list(combinations(boards, 2))

    for f in sorted(files.iterdir()):
        # Counter used to check how many pairs have been calculated
        pair_counter = 0

        for (board1, board2) in boards_combs:
            print(f'\r[{pair_counter}/{len(boards_combs)}] {f}', end='')

            region_df = pd.read_json(f)

            b1_df = region_df[region_df["Board"] == board1].iloc[1, :]
            b2_df = region_df[region_df["Board"] == board2].iloc[1, :]

            dist = hamming(b1_df["Data"], b2_df["Data"])

            uniq = (dist * 100) / CHUNK_SIZE
            out_f.write(f'{b1_df["Board"]},{b2_df["Board"]},{b1_df["Mem_pos"]},{uniq}\n')

            pair_counter += 1

    out_f.close()


if __name__ == '__main__':
    calculate_uniqueness(32)
    calculate_uniqueness(64)
