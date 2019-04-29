#!/usr/bin/env python

# encoding: utf-8

'''

@author: Jason Lee

@license: (C) Copyright @ Jason Lee

@contact: jiansenll@163.com

@file: jianzhi_offer_64.py

@time: 2019/4/28 23:24

@desc:

'''

from max_heap import max_heap
from min_heap import min_heap

class Solution:
    def __init__(self):
        self.max = []
        self.min = []
        self.count = 0

    def Insert(self, num):
        self.count += 1
        if self.count % 2 != 0:
            self.max.append(num)
        else:
            self.min.append(num)

    def GetMedian(self):
        if self.count == 1:
            return self.max[0]
        max_heap(self.max)
        min_heap(self.min)
        while self.max[0] > self.min[0]:
            self.max[0], self.min[0] = self.min[0], self.max[0]
            max_heap(self.max)
            min_heap(self.min)

        if self.count % 2 != 0:
            return self.max[0]
        else:
            return (self.max[0] + self.min[0]) / 2.0