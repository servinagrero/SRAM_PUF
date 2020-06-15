#!/usr/bin/env python3
#
# Class to store memory dumps from the boards

from datetime import datetime


class Dump(object):

    def __init__(self, board_id,
                 data, mem_pos, temp, vdd,
                 temp_cal_30, temp_cal_110, vrefint_cal,
                 length=None, timestamp=None):
        self.Board = board_id
        self.Temp = temp
        self.Vdd = vdd
        self.Temp_cal_30 = temp_cal_30
        self.Temp_cal_110 = temp_cal_110
        self.Vrefint_cal = vrefint_cal
        self.Timestamp = datetime.now().strftime('%d-%m-%Y-%H:%M:%S')
        self.Mem_pos = mem_pos
        self.Data = data
        self.Length = len(data) if length is None else length

    def __eq__(self, other):
        if self.Length != other.Length:
            raise ValueError("The length of the dumps is not the same")

        for i in range(0, self.Length):
            if self.Data[i] != other.Data[i]:
                return False
        else:
            return True


def compare_dumps(dump1, dump2):
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
