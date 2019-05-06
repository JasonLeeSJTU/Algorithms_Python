#!/usr/bin/env python

# encoding: utf-8

'''

@author: Jason Lee

@license: (C) Copyright @ Jason Lee

@contact: jiansenll@163.com

@file: jianzhi_offer_32.py

@time: 2019/5/6 15:40

@desc:

'''


class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        i = 1
        count = 0
        while i <= n:
            base = i*10
            temp = n % base
            residual = i if temp >= 2 * i - 1 else 0 if temp <= i - 1 else temp - i + 1
            count += (n // base) * i + residual
            i *= 10

        return count

if __name__ == '__main__':
    res = Solution()
    a = res.NumberOf1Between1AndN_Solution(13)
    print(a)