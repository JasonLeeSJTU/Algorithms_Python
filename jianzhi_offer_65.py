#!/usr/bin/env python

# encoding: utf-8

'''

@author: Jason Lee

@license: (C) Copyright @ Jason Lee

@contact: jiansenll@163.com

@file: jianzhi_offer_65.py

@time: 2019/4/25 13:00

@desc:

'''

class Solution:
    def maxInWindows(self, num, size):
        if not num or size <= 0:
            return []
        if size > len(num):
            return []
        if size == 1:
            return num

        f = max(num[0:size-1])
        res = []
        for i in range(size-1, len(num)):
            temp = max(f, num[i])
            res.append(temp)
            if temp != f:
                f = temp
            else:
                f = max(num[i-size+2:i+1])

        return res

if __name__ == '__main__':
    num = [2,3,4,2,6,2,5,1]
    res = Solution()
    a = res.maxInWindows(num, 3)
    print(a)

