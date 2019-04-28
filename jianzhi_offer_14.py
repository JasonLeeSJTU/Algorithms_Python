#!/usr/bin/env python

# encoding: utf-8

'''

@author: Jason Lee

@license: (C) Copyright @ Jason Lee

@contact: jiansenll@163.com

@file: jianzhi_offer_14.py

@time: 2019/4/28 22:54

@desc:

'''

class Solution:
    def reOrderArray(self, array):
        odd = []
        even = []
        for item in array:
            if item % 2 != 0:
                odd.append(item)
            else:
                even.append(item)

        return odd + even


if __name__ == '__main__':
    res = Solution()
    a = res.reOrderArray([1,2,3,4,5,6,7])
    print(a)