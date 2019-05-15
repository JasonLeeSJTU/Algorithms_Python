#!/usr/bin/env python

# encoding: utf-8

'''

@author: Jason Lee

@license: (C) Copyright @ Jason Lee

@contact: jiansenll@163.com

@file: jianzhi_offer_11.py

@time: 2019/5/15 13:58

@desc:

'''
class Solution:
    def Power(self, base, exponent):
        if base == 0 and exponent <= 0:
            return None

        expo = exponent
        if exponent < 0:
            expo = -exponent

        # res = 1
        # while expo:
        #     res *= base
        #     expo -= 1
        res = self.power(base, expo)

        return res if exponent >= 0 else 1/res

    def power(self, base, exponent):
        if exponent == 0:
            return 1
        if exponent == 1:
            return base
        res = self.power(base, exponent >> 1)
        res *= res
        if exponent & 0x1 == 1: # exponent是奇数，则a^n = a^(n/2) * a^(n/2) * a，否则a^n = a^(n/2) * a^(n/2)
            res *= base

        return res