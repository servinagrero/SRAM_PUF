#!/usr/bin/env python

import pandas as pd
import numpy as np
from pathlib import Path
from collections import Counter

CHUNK_SIZE = 4096


def hamming(v1, v2):
    '''Hamming Distance between two vectors'''
    return sum(map(np.int64.__ne__, v1, v2))


def calculate_rel_per_bit(bType):
    '''
    Calculate the reliability per bit for all boards

    ReliabilityPerBit is calculated similar to reliability but taking into
    account all boards.
    '''
    out_f = open(f'../data/processed/reliability_per_bit_{bType}.csv', "w")
    out_f.write('Board,Mem_pos,Bit,Bit_Ref,ReliabilityPerBit\n')

    ref_samples = pd.read_csv(f"../data/interim/references_samples_{bType}.csv")
    files = Path(f'../data/raw/{bType}')

    bitOffset = 0
    for f in sorted(files.iterdir()):
        mem_pos = str(f)[-15:-5]
        print(f'Region: {mem_pos}')

        samples = pd.read_json(f)
        ref_samples_region = ref_samples[ref_samples['Mem_pos'] == mem_pos]

        for board, grouped in samples.groupby(['Board']):
            bins = np.array(grouped['Data'].to_list()).T
            ref_samples_board = ref_samples_region[ref_samples_region['Board'] == board]
            bits_ref = ref_samples_board['Bit_Ref'].to_list()

            for bit, row in enumerate(bins):
                bit_ref = bits_ref[bit]
                rel = get_reliability(bit_ref, row)
                out_f.write(f'{board},{mem_pos},{bit + (bitOffset * CHUNK_SIZE)},{bit_ref},{rel}\n')

        bitOffset += 1


def get_reliability(bit_ref, row):
    '''Calculate the reliability depending on the reference bit.'''
    rel = sum(row) * 100 / len(row)
    rel = 100 - rel if bit_ref == 0 else rel
    return rel


def generate_summary(bType):
    '''
    Generate summaries for each board type.

    The summary is the mean of each ReliabilityPerBit
    '''

    rpb_df = pd.read_csv(f'../data/processed/reliability_per_bit_{bType}.csv')
    rpb_mean_df = pd.DataFrame(columns=['Mem_pos', 'Bit', 'Bit_Ref', 'ReliabilityPerBit'])

    for bit, grouped in rpb_df.groupby('Bit'):
        mean = grouped.ReliabilityPerBit.mean()
        cnt = Counter(grouped.Bit_Ref.to_list())

        data = {
            'Mem_pos': grouped.iloc[0, :]['Mem_pos'],
            'Bit': bit,
            'Bit_Ref': cnt.most_common()[0][0],
            'ReliabilityPerBit': mean
        }

        rpb_mean_df = rpb_mean_df.append(data, ignore_index=True)

    rpb_mean_df.to_csv(f'../data/processed/reliability_per_bit_mean_{bType}.csv')


if __name__ == '__main__':
    for bType in [32, 64]:
        calculate_rel_per_bit(bType)
        generate_summary(bType)
