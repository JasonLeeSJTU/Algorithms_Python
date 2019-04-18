#!/usr/bin/env python

# encoding: utf-8

'''

@author: Jason Lee

@license: (C) Copyright @ Jason Lee

@contact: jiansenll@163.com

@file: jianzhi_offer_3.py

@time: 2019/4/18 11:03

@desc:

'''

class Solution:
    # array 二维列表
    def Find(self, target, array):
        if not target or not array:
            return False

        rows = len(array)
        cols = len(array[0])

        row = rows - 1
        col = 0
        while col < cols and row >= 0:
            if target == array[row][col]:
                return True
            elif target > array[row][col]:
                col += 1
            else:
                row -= 1

        return False

if __name__ == '__main__':
    array = [[1,2,8,9],[2,4,9,12],[4,7,10,13],[6,8,11,15]]
    res = Solution()
    a = res.Find(16, array)
    print(a)
