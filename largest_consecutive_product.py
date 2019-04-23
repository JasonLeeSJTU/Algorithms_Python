#!/usr/bin/env python

# encoding: utf-8

'''

@author: Jason Lee

@license: (C) Copyright @ Jason Lee

@contact: jiansenll@163.com

@file: largest_consecutive_product.py

@time: 2019/4/23 16:36

@desc:

'''

def max_product(array):
    if not array:
        return 0
    fmax = [array[0]] * len(array)
    fmin = [array[0]] * len(array)
    for i in range(1, len(array)):
        fmin[i] = min(fmin[i-1]*array[i], fmax[i-1]*array[i], array[i])
        fmax[i] = max(fmax[i-1]*array[i], fmin[i-1]*array[i], array[i])
    return max(fmax)

if __name__ == '__main__':
    array = [1, 2, 0, -1, -3, -2]
    a = max_product(array)
    print(a)