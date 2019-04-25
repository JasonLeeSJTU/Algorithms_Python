#!/usr/bin/env python

# encoding: utf-8

'''

@author: Jason Lee

@license: (C) Copyright @ Jason Lee

@contact: jiansenll@163.com

@file: jianzhi_offer_65_1.py

@time: 2019/4/25 15:29

@desc:

'''
class Solution:
    def maxInWindows(self, num, size):
        if not num or size <= 0:
            return []
        if size > len(num):
            return []
        if size == 1:
            return num

        idx = []    # queue stores index, max value in [0]
        res = []    # results

        # first size numbers
        for i in range(size):
            while idx and num[i] >= num[idx[-1]]:
                idx.pop()
            idx.append(i)   # only store index

        res.append(num[idx[0]])     # the first max value in the first sliding window
        # other numbers
        for i in range(size, len(num)):
            if idx[0] <= i - size:      # index[0] is out of the window
                idx.pop(0)
            while idx and num[i] >= num[idx[-1]]:
                idx.pop()
            idx.append(i)
            res.append(num[idx[0]])

        return res

if __name__ == '__main__':
    num = [2,3,4,2,6,2,5,1]
    res = Solution()
    a = res.maxInWindows(num, 3)
    print(a)
