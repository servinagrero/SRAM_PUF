#!/usr/bin/python

import numpy as np
import pandas as pd
from collections import Counter
from pathlib import Path


def calculate_reference_samples(bType):
    '''
    Calculate the references bits for each board.
    This is later used to calculate the rest of the parameters.

    Each bit is calculated by counting the number of `0` and `1` for each bit
    across all samples. The reference bit is the most common one.
    '''

    files = Path(f"../data/raw/{bType}")

    out_f = open(f'../data/processed/references_samples_{bType}.csv', "w")
    out_f.write('Board,Mem_pos,Bit_In_Region,Bit,Bit_Ref\n')

    # bitOffset used to calculate the global bit position
    bitOffset = 0

    for f in sorted(files.iterdir()):
        mem_region = str(f)[-15:-5]
        print(f'Region: {mem_region}')

        data = pd.read_json(f)

        for board, grouped in data.groupby('Board'):

            # Extract all samples as an NxM matrix
            # Where N = 4096 and N = number of samples
            bins = np.array(grouped.Data.to_list()).T

            for bit, bit_rows in enumerate(bins):
                counter = Counter(bit_rows)
                ref_bit = counter.most_common()[0][0]
                out_f.write(f'{board},{mem_region},{bit},{bit + (bitOffset * 4096)},{ref_bit}\n')

        bitOffset += 1


if __name__ == '__main__':
    calculate_reference_samples(32)
    calculate_reference_samples(64)
