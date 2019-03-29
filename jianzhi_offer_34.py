#!/usr/bin/env python

# encoding: utf-8

'''

@author: Jason Lee

@license: (C) Copyright @ Jason Lee

@contact: jiansenll@163.com

@file: jianzhi_offer_34.py

@time: 2019/3/29 10:06

@desc:

'''

def GetUglyNumber_Solution(index):
    if not index:
        return 0

    ugly_number = [0]*index
    ugly_number[0] = 1
    idx2 = 0
    idx3 = 0
    idx5 = 0
    idx = 1
    while idx < index:
        ugly_number[idx] = min(ugly_number[idx2]*2, ugly_number[idx3]*3, ugly_number[idx5]*5)
        # forward one step if factor 2 is used
        while ugly_number[idx2]*2 <= ugly_number[idx]:
            idx2 += 1
        # forward one step if factor 3 is used
        while ugly_number[idx3]*3 <= ugly_number[idx]:
            idx3 += 1
        # factor 5
        while ugly_number[idx5]*5 <= ugly_number[idx]:
            idx5 += 1
        idx += 1

    return ugly_number[index - 1]


if __name__ == '__main__':
    a = GetUglyNumber_Solution(1500)
    print(a)