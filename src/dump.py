#!/usr/bin/env python3
#
# Class to store memory dumps from the boards

from itertools import combinations
from datetime import datetime


class Dump():

    def __init__(self, board_id,
                 data, mem_pos, temp, vdd,
                 temp_cal_30, temp_cal_110, vrefint_cal,
                 length=None, fd=None, timestamp=None):

        self.board_id = board_id
        self.temp = temp
        self.vdd = vdd
        self.temp_cal_30 = temp_cal_30,
        self.temp_cal_110 = temp_cal_110,
        self.vrefint_cal = vrefint_cal,
        self.timestamp = datetime.now().strftime('%d-%m-%Y-%H:%M:%S')
        self.mem_pos = mem_pos
        self.data = data
        self.length = len(data) if length is None else length

    def __eq__(self, other):
        if self.length != other.length:
            raise ValueError("The length of the dumps is not the same")

        for i in range(0, self.length):
            if self.data[i] != other.data[i]:
                return False
        else:
            return True

    def __dict__(self):
        return {'board_id': self.board_id,
                'mem_pos': self.mem_pos,
                'temp': self.temp,
                'vdd': self.vdd,
                'temp_cal_30': self.temp_cal_30,
                'temp_cal_110': self.temp_cal_110,
                'vrefint_cal': self.vrefint_cal,
                'length': self.length,
                'timestamp': self.timestamp,
                'data': self.data
                }


def compare_files(dump1, dump2):
    '''
    Calculate by how much two dumps differ
    '''
    differ = 0
    if dump1.lenght != dump2.lenght:
        raise ValueError("The length of the dumps differs.")

    for i in range(0, dump1.length):
        if dump1[i] != dump2[i]:
            differ += 1
    return (differ / dump1.length) * 100


def create_files_combinations(dumps_lists):
    '''
    Given a lists of memory dumps, return every pair
    combition possible.
    '''
    return list(combinations(dumps_lists, 2))


def filter_results(dumps_list, threshold=20):
    '''
    Given a list of dumps and its difference,
    keep the pairs that are lower than a given threshold.
    '''
    final_list = []
    for i, (d1, d2, d) in enumerate(dumps_list):
        if d < threshold:
            final_list.append((d1, d2, d))
    return final_list
