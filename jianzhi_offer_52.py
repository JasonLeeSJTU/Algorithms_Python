#!/usr/bin/env python

# encoding: utf-8

'''

@author: Jason Lee

@license: (C) Copyright @ Jason Lee

@contact: jiansenll@163.com

@file: jianzhi_offer_52.py

@time: 2019/5/15 14:46

@desc:

'''

class Solution:
    def multiply(self, A):
        # 先从左向右乘一遍，再从右向左乘一遍
        if not A:
            return None
        if len(A) == 1:
            return 0

        B = [1 for i in range(len(A))]
        temp = 1
        for i in range(1, len(A)):
            temp *= A[i-1]
            B[i] = temp

        temp = 1
        for i in range(len(A)-2, -1, -1):
            temp *= A[i+1]
            B[i] *= temp

        return B

if __name__ == '__main__':
    A = [1]
    res = Solution()
    B = res.multiply(A)
    print(B)