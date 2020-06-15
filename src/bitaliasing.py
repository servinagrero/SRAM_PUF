#!/usr/bin/python

import pandas as pd

CHUNK_SIZE = 4096  # Size of each sample


def calculate_bitaliasing(bType):
    '''
    Calculate the bitaliasing for boards of type `bType`.
    If bitaliasing happens, different chips will produce similar responses.

    Bitaliasing is calculated as the sum of the nth bit of the response across all boards.
    '''

    out_f = open(f'../data/processed/bitaliasing_{bType}.csv', "w")
    out_f.write('Mem_Region,Bit,BitAliasing\n')

    samples = pd.read_csv(f"../data/interim/references_samples_{bType}.csv")
    regions = pd.read_csv(f'../data/interim/regions_{bType}.csv')
    regions = regions.columns.to_list()

    # bitOffset is used to print the global bit position
    bitOffset = 0

    for mem_region in regions:
        print(f'Region: {mem_region}')
        region_samples = samples[samples['Mem_pos'] == mem_region]

        for bit, group in region_samples.groupby('Bit_In_Region'):
            bins = group.Bit_Ref.to_list()
            bitalias = sum(bins) * 100 / len(bins)
            out_f.write(f'{mem_region},{bit + (bitOffset * CHUNK_SIZE)},{bitalias}\n')

        bitOffset += 1


if __name__ == '__main__':
    calculate_bitaliasing(32)
    calculate_bitaliasing(64)
