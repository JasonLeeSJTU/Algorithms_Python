#!/usr/bin/env python

# encoding: utf-8

'''

@author: Jason Lee

@license: (C) Copyright @ Jason Lee

@contact: jiansenll@163.com

@file: quick_sort.py

@time: 2019/3/28 10:13

@desc:

'''


def quick_sort(data):
    if len(data) == 1:
        return
    quick_sort_core(data, 0, len(data) - 1)


def quick_sort_core(data, start, end):
    if len(data) == 1:
        return
    id = partition(data, start, end)
    if id > start:
        quick_sort_core(data, start, id - 1)
    if id < end:
        quick_sort_core(data, id + 1, end)


def partition(data, left, right):
    # compared with data[0], i starts from left, j starts from right
    i = left
    j = right
    while True:
        while data[i] <= data[left] and i < right:
            i += 1
        while data[j] > data[left] and j > left:
            j -= 1
        # stop when i meets j
        if i >= j:
            break

        data[i], data[j] = data[j], data[i]

    data[left], data[j] = data[j], data[left]
    return j

if __name__ == '__main__':
    data = [1]
    quick_sort(data)
    print(data)