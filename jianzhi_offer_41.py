#!/usr/bin/env python

# encoding: utf-8

'''

@author: Jason Lee

@license: (C) Copyright @ Jason Lee

@contact: jiansenll@163.com

@file: jianzhi_offer_41.py

@time: 2019/5/2 13:14

@desc:

'''
class Solution:
    def FindContinuousSequence(self, tsum):
        # 根据等差数列的求和公式 s = n*a_1 + n*(n-1)/2
        res = []
        n = 2   # numbers
        while n*(n-1)/2 < tsum:
            na1 = tsum - n*(n-1)/2
            if na1 % n == 0:    #整除，说明此序列满足条件
                a1 = na1/n
                temp = []
                for i in range(n):
                    temp.append(a1 + i)
                res.append(temp)

            n += 1

        return sorted(res, key=lambda c: c[0])

if __name__ == '__main__':
    res = Solution()
    a = res.FindContinuousSequence(15)
    print(a)
