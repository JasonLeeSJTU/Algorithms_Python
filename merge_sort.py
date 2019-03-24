#!/usr/bin/env python

# encoding: utf-8

'''

@author: Jason Lee

@license: (C) Copyright @ Jason Lee

@contact: jiansenll@163.com

@file: merge_sort.py

@time: 2019/3/24 20:21

@desc:

'''
import numpy as np


def merge_sort(data):
    return sort(data)


def sort(data):
    if len(data) <= 1:
        return data

    mid = len(data) // 2

    left = sort(data[:mid])
    right = sort(data[mid:])

    return merge(left, right)


def merge(left, right):
    temp = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            temp.append(left[i])
            i = i + 1
        else:
            temp.append(right[j])
            j = j + 1

    while i < len(left):
        temp.append(left[i])
        i = i + 1

    while j < len(right):
        temp.append(right[j])
        j = j + 1

    return temp


if __name__ == '__main__':
    a = np.random.randint(10, size=10)
    b = merge_sort(a)
    print(a)
    print(b)
    print(a)
