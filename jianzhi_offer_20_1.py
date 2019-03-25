#!/usr/bin/env python

# encoding: utf-8

'''

@author: Jason Lee

@license: (C) Copyright @ Jason Lee

@contact: jiansenll@163.com

@file: jianzhi_offer_20.py

@time: 2019/3/25 14:26

@desc:
题目描述:

输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字，
例如，如果输入如下4 X 4矩阵： 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16
则依次打印出数字1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10.

Another solution by matrix flipping -90 degree
'''

import numpy as np
from functools import reduce

def clockwise_print_matrix(matrix):
    temp = []
    while True:
        temp.append(matrix[0])
        matrix.pop(0)
        if not len(matrix):
            break

        matrix = np.transpose(matrix).tolist()
        matrix = matrix[::-1]

    return reduce(lambda x,y:x+y, temp)


if __name__ == '__main__':
    #a=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
    #a = [[1], [2], [3], [4], [5]]
    #a=[[1]]
    a = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]
    print(a[::])
    print(clockwise_print_matrix(a))
