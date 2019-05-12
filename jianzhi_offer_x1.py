#!/usr/bin/env python

# encoding: utf-8

'''

@author: Jason Lee

@license: (C) Copyright @ Jason Lee

@contact: jiansenll@163.com

@file: jianzhi_offer_x1.py

@time: 2019/5/12 20:45

@desc:

'''


class Solution:
    def jumpFloorII(self, number):
        if number == 0:
            return 0
        if number == 1:
            return 1
        res = [1, 1]  # f(0) = 1
        # f(n) = f(n-1) + f(n-2) + ... + f(0)
        for i in range(2, number + 1):
            temp = sum(res)
            res.append(temp)

        return res[-1]

    # f(n) = 2^(n-1)
    def another(self, number):
        if number == 0:
            return 0
        return 1 << (number - 1)
