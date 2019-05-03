#!/usr/bin/env python

# encoding: utf-8

'''

@author: Jason Lee

@license: (C) Copyright @ Jason Lee

@contact: jiansenll@163.com

@file: jianzhi_offer_49.py

@time: 2019/5/3 14:52

@desc:

'''
import re
class Solution:
    def StrToInt(self, s):
        number = list('0123456789')
        pattern = re.compile(r'^[+-]?[0-9]+$')
        res = pattern.match(s)
        if not res:
            return 0
        else:
            temp = list(s)
            num = 0
            label = 1
            if temp[0] == '-':
               label = -1
            elif temp[0] == '+':
               label = 1
            else:
                num = number.index(temp[0])
            for i in range(1, len(temp)):
                num = num*10 + number.index(temp[i])

        return num * label


if __name__ == '__main__':
    res = Solution()
    a = res.StrToInt('-123')
    print(a)