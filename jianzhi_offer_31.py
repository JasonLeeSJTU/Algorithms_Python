#!/usr/bin/env python

# encoding: utf-8

'''

@author: Jason Lee

@license: (C) Copyright @ Jason Lee

@contact: jiansenll@163.com

@file: jianzhi_offer_31.py

@time: 2019/4/23 16:09

@desc:

'''
class Solution:
    def FindGreatestSumOfSubArray(self, array):
        if not array:
            return 0

        f = array
        for i in range(1, len(array)):
            if f[i-1] <= 0:
                f[i] = array[i]
            else:
                f[i] = f[i-1] + array[i]

        return max(f)

if __name__ == '__main__':
    res = Solution()
    array = [6,-3,-2,7,-15,1,2,2]
    b = res.FindGreatestSumOfSubArray(array)
    print(b)

