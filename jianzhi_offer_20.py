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
'''


def clockwise_print_matrix(matrix):
    temp = []
    while True:
        if not len(matrix[0]):
            break

        while len(matrix[0]):
            temp.append(matrix[0].pop(0))
        matrix.pop(0)
        for i in range(len(matrix)):
            temp.append(matrix[i].pop())

        if not len(matrix):
            break
        if len(matrix[0]) == 0:
            break

        if len(matrix):
            while len(matrix[-1]):
                temp.append(matrix[-1].pop())
            matrix.pop()
        else:
            break

        if len(matrix):
            for i in range(len(matrix) - 1, -1, -1):
                temp.append(matrix[i].pop(0))
        else:
            break

    return temp


if __name__ == '__main__':
    # a=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
    # a = [[1], [2], [3], [4], [5]]
    # a=[[1]]
    a = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]
    print(a)
    print(clockwise_print_matrix(a))
