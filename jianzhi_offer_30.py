#!/usr/bin/env python

# encoding: utf-8

'''

@author: Jason Lee

@license: (C) Copyright @ Jason Lee

@contact: jiansenll@163.com

@file: jianzhi_offer_30.py

@time: 2019/3/28 12:49

@desc:

'''

import random
def GetLeastNumbers_Solution(tinput, k):
    if k > len(tinput):
        return []
    if k == 0:
        return []

    id = partition(tinput, 0, len(tinput) - 1)
    while id + 1 != k:
        if id + 1 > k:
            id = partition(tinput, 0, id - 1)
        if id + 1 < k:
            id = partition(tinput, id + 1, len(tinput) - 1)

    return tinput[:id + 1]


def partition(data, left, right):
    # compared with data[0], i starts from left, j starts from right
    i = left
    j = right
    idx = random.randint(left, right)
    while True:
        while data[i] <= data[idx] and i < right:
            i += 1
        while data[j] > data[idx] and j > left:
            j -= 1
        # stop when i meets j
        if i >= j:
            break

        data[i], data[j] = data[j], data[i]

    data[idx], data[j] = data[j], data[idx]
    return j

if __name__ == '__main__':
    a = [4,5,1,6,2,7,3,8]
    b = GetLeastNumbers_Solution(a, 0)
    print(b)