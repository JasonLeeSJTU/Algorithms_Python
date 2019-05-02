#!/usr/bin/env python

# encoding: utf-8

'''

@author: Jason Lee

@license: (C) Copyright @ Jason Lee

@contact: jiansenll@163.com

@file: jianzhi_offer_41_1.py

@time: 2019/5/2 13:52

@desc:

'''
class Solution:
    def FindNumbersWithSum(self, array, tsum):
        if not array:
            return []
        if len(array) == 1:
            return []

        res = []
        left = 0
        right = len(array) - 1
        while right > left:
            if array[left] + array[right] > tsum:
                right -= 1
            elif array[left] + array[right] < tsum:
                left += 1
            else:
                res.append([array[left], array[right]])
                break
                right -= 1

        return res

if __name__ == '__main__':
    res = Solution()
    a = res.FindNumbersWithSum([1,2,4,7,8,11,15], 15)
    print(a)
