#!/usr/bin/env python3

from datetime import datetime


class Sample(object):
    """
    Sample represents a final dump of data.
    It has the following fields:
      - All the parameters from the board
      - All the data from the dump
      - All the bits from the data dump
      - Timestamp and Datetime from the dump
    """

    def __init__(self, sample):
        self.__dict__ = sample
        self._id
        self.Board
        self.Wafer
        self.Lot
        self.Y
        self.X
        self.Type
        self.Mem_pos
        self.Temp
        self.Vdd
        self.Temp_cal_30
        self.Temp_cal_110
        self.Vrefint_cal
        self.Timestamp
        self.Data
        self.Datetime = datetime.strptime(sample["Timestamp"], "%d-%m-%Y-%H:%M:%S")

    def __xor__(self, other):
        pass

    def uniformity(self):
        return sum(self.Data) / len(self.Data) * 100

    @staticmethod
    def uniform(arr):
        return sum(arr) / len(arr) * 100

    @staticmethod
    def hamming(s1, s2):
        return sum(map(int.__ne__, s1.Data, s2.Data))
