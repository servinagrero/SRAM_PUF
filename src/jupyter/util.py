#!/usr/bin/env python

import pymongo

import multiprocessing as mp
from itertools import combinations

import pandas as pd

import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

import bokeh.plotting as bplt
import bokeh.models as bmods
import bokeh.io as bio


def add_to_off(address, starting_address=0x20000000, dump_size=512):
    '''Convert a memory address into an index.'''
    if isinstance(address, str):
        address = int(address, 16)
    if isinstance(starting_address, str):
        starting_address = int(starting_address, 16)

    return (address - starting_address) // dump_size


def off_to_add(offset, starting_address=0x20000000, dump_size=512):
    '''Convert an offset into a memory address.'''
    if isinstance(starting_address, str):
        starting_address = int(starting_address, 16)

    return hex(offset * dump_size + starting_address)


def parallelize_call_ma(func, func_args, pool_count=mp.cpu_count()):
    '''Use multiprocessing to parallelize the call to func'''
    pool = mp.Pool(pool_count)
    results = [pool.map_async(func, func_args)]
    pool.close()
    pool.join()

    return [p.get() for p in results]


def plot_memory_regions_bokeh(board_id, offset=0, mem_ending_pos=32,
                              chunk_size=512, show_every=False):
    '''
    Given a board id, make a scatter plot of the specified memory dumps.
    X axis is the direction and the y axis is the value at that position.
    '''

    client = pymongo.MongoClient("mongodb://localhost:27017/")
    database = client['thesis']
    db_dumps = database['dumps']

    mem_pos, mem_off, mem_val = [], [], []

    dumps_list = list(db_dumps.find({"board_id": board_id}))

    for plot in range(offset, mem_ending_pos):
        mem_val = dumps_list[plot]['data']
        mem_off = dumps_list[plot]['mem_pos']
        mem_pos = [int(mem_off, 16) + i for i in range(0, chunk_size)]

        source = bplt.ColumnDataSource(data=dict(
            address=mem_pos,
            value=mem_val,
        ))

        hover = bmods.HoverTool(
            tooltips=[
                ("Address", "@address{0x%X}"),
                ("Value", "@value"),
            ],
            formatters={'address': 'printf'},
        )

        tools = [hover, 'pan', 'box_zoom', 'wheel_zoom', 'save', 'reset']
        # Generate the plot
        title = f'[{board_id}] Memory map at {mem_off}'

        p = bplt.figure(plot_width=1000, plot_height=500,
                        y_range=(-5, 270),
                        tools=tools,
                        title=title)

        p.circle(x='address', y='value', size=5, source=source)
        p.xaxis[0].formatter = bmods.PrintfTickFormatter(format="0x%X")
        # p.circle(mem_pos, mem_val, size=8)

        if show_every:
            bio.show(p)


# TODO: Use bokeh for interactive plots
def plot_memory_regions(board_id, offset=0, mem_ending_pos=32,
                        chunk_size=512, show_every=False):
    '''
    Given a board id, make a scatter plot of the specified memory dumps.
    X axis is the direction and the y axis is the value at that position.
    '''

    client = pymongo.MongoClient("mongodb://localhost:27017/")
    database = client['thesis']
    db_dumps = database['dumps']

    mem_pos, mem_off, mem_val = [], [], []

    dumps_list = list(db_dumps.find({"board_id": board_id}))

    for plot in range(offset, mem_ending_pos):
        mem_val = dumps_list[plot]['data']
        mem_off = dumps_list[plot]['mem_pos']
        mem_pos = [int(mem_off, 16) + i for i in range(0, chunk_size)]

        # Generate the plot
        plt.scatter(mem_pos, mem_val, marker='x')
        plt.xlabel('Memory address')
        plt.ylabel('Values')

        if show_every:
            plt.title('[' + board_id + '] Memory map at ' + str(mem_off))
        else:
            starting_address = off_to_add(offset)
            ending_address = off_to_add(mem_ending_pos)
            plt.title('[' + board_id + '] Memory map from ' +
                      str(starting_address) + ' to ' + str(ending_address))

        ax = plt.gca()
        plt.ylim((0, 270))

        ax.xaxis.set_major_locator(plt.MaxNLocator(16))
        ax.yaxis.set_major_locator(plt.MaxNLocator(25))
        ax.xaxis.set_minor_locator(ticker.AutoMinorLocator(10))
        ax.yaxis.set_minor_locator(ticker.AutoMinorLocator(5))

        xlabels = map(lambda t: '0x%08X' % int(t), ax.get_xticks())
        ax.set_xticklabels(xlabels, rotation=45, horizontalalignment='right')

        plt.grid()

        # Show every plot or all of the data combined in one
        if show_every:
            plt.show()


def calculate_diff(sample1, sample2):
    '''
    Given two dumps of data, calculate the difference between their data.
    '''
    diff = 0
    length = min(sample1['length'], sample2['length'])

    for i in range(length):
        if sample1['data'][i] != sample2['data'][i]:
            diff = diff + 1

    diff = diff / int(sample1['length'])
    return (diff * 100)


def compare_dumps_one_board(board_id, df=None, board_dumps=[]):
    '''
    Given a pair of dumps of a board, calculate the difference in % between
    them. Outputs a data frame with the board_id, the memory position
    and the difference in % between the samples.
    '''
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    database = client['thesis']
    db_dumps = database['dumps']

    if df is None:
        column_names = ["Board", "Region", "Id_1", "Id_2", "Diff"]
        df = pd.DataFrame(columns=column_names)

    if not board_dumps:
        board_dumps = db_dumps.find({"board_id": board_id})

    # Every possible starting memory address
    memory_regions = list(set([mem_pos['mem_pos'] for mem_pos in board_dumps]))

    # There are 32 groups, one per region of memory
    for region in memory_regions:

        samples = list(db_dumps.find({"mem_pos": region,
                                      "board_id": board_id}))
        region_samples = list(combinations(samples, 2))

        # Cycle through all of the samples of that memory region
        for i, (sample1, sample2) in enumerate(region_samples):
            diff = calculate_diff(sample1, sample2)

            data = {'Board': board_id,
                    'Region': region,
                    'Id_1': str(sample1['_id']),
                    'Id_2': str(sample2['_id']),
                    'Diff': diff}
            # db_comps.insert_one(data)
            df = df.append(data, ignore_index=True)

    return df


def filter_results_df(data_frame, lower_thresh, upper_thresh, column='Diff'):
    '''
    Filter the results of a data frame.
    The new data frame has values between the given thresholds.
    '''
    is_valid = data_frame[column] > lower_thresh
    data_frame = data_frame[is_valid]

    is_valid = data_frame[column] < upper_thresh
    data_frame = data_frame[is_valid]

    return data_frame
