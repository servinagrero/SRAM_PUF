#!/usr/bin/python

import pandas as pd

from pathlib import Path

CHUNK_SIZE = 4096  # Size of each sample


def hamming(v1, v2):
    '''Hamming Distance between two vectors'''
    return sum(map(int.__ne__, v1, v2))


def calculate_reliability(bType):
    '''
    Calculate the reliability of each sample for every board.

    Reliability is calculated as 100 minus the hamming distance between the
    reference sample and every other sample.

    The id of each sample is the id from the Mongo db.
    '''
    out_f = open(f'../data/processed/reliability_per_bit_{bType}.csv', "w")
    out_f.write('Board,Mem_pos,Ref_sample,Sample,Reliability\n')

    files = Path(f"../data/raw/{bType}")

    boards_df = pd.read_csv("./boards_{bType}.csv").columns.to_list()
    ref_samples = pd.read_csv(f'./reference_samples_{bType}.csv')

    for f in sorted(files.iterdir()):
        mem_pos = str(f)[-15:-5]
        print(f'Region: {mem_pos}')

        region_df = pd.read_json(f)
        region_df.set_index("_id", inplace=True)
        ref_samples_region = ref_samples[ref_samples['Mem_pos'] == mem_pos]

        for board, grouped in region_df.groupby('Board'):
            ref_sample = ref_samples_region[ref_samples_region['Board'] == 'Board']

            for idx in range(2, len(grouped.index)):
                rel = hamming(ref_sample["Data"], grouped.iloc[id, :]["Data"])
                rel = 100 - (rel * 100 / CHUNK_SIZE)
                sample_id = boards_df.iloc[id, :].name
                out_f.write(f'{board},{mem_pos},{idx},{sample_id},{rel}\n')

    out_f.close()


if __name__ == '__main__':
    calculate_reliability(32)
    calculate_reliability(64)
