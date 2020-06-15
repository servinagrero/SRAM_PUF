#!/usr/bin/python

import pandas as pd
from pathlib import Path

CHUNK_SIZE = 4096


def calculate_uniformity(bType):
    '''
    Calculate the uniformity for each simple.

    Only the uniformity is calculated. Later,the samples_list and uniformity csv are merged into one.
    '''

    files = Path(f"../data/raw/{bType}")

    out_f = open(f'../data/processed/uniformity_raw_{bType}.csv', "w")
    out_f.write('_id,Uniformity\n')

    for f in sorted(files.iterdir()):
        mem_region = str(f)[-15:-5]
        print(f'Region: {mem_region}')

        samples = pd.read_json(f)

        for _, sample in samples.iterrows():
            unif = (sum(sample['Data']) / CHUNK_SIZE) * 100
            out_f.write(f'{sample["_id"]},{unif}\n')


def join_csv(bType):
    '''
    Join the samples and the uniformity csv into a final file.
    '''
    samples = pd.read_csv('../data/interim/samples_list.csv')
    samples_df = samples[samples['Type'] == bType]
    unif_df = pd.read_csv(f'../data/processed/uniformity_raw_{bType}.csv')

    samples.set_index('_id', inplace=True)
    unif_df.set_index('_id', inplace=True)

    samples_df.join(unif_df)

    samples_df.to_csv(f'../data/processed/uniformity_{bType}.csv',
                      index=True)

    # Remove the raw file since it is no longer needed
    unif_raw_f = Path('../data/processed/uniformity_raw_{bType}.csv')
    unif_raw_f.unlink(missing_ok=True)


if __name__ == '__main__':
    for bType in [32, 64]:
        calculate_uniformity(bType)
        join_csv(bType)
