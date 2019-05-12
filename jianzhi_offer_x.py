#!/usr/bin/env python

# encoding: utf-8

'''

@author: Jason Lee

@license: (C) Copyright @ Jason Lee

@contact: jiansenll@163.com

@file: jianzhi_offer_x.py

@time: 2019/5/12 20:32

@desc:

'''


class Solution:
    def jumpFloor(self, number):
        if number == 1:
            return 1
        if number == 2:
            return 2

        # f(n) = f(n-1) + 1 + f(n-2) + 2
        a = 1
        b = 2
        for i in range(2, number):
            a, b = b, a + b + 3
        return b
