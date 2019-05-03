#!/usr/bin/env python

# encoding: utf-8

'''

@author: Jason Lee

@license: (C) Copyright @ Jason Lee

@contact: jiansenll@163.com

@file: jianzhi_offer_54.py

@time: 2019/5/3 13:36

@desc:

'''
import re
class Solution:
    # s字符串
    def isNumeric(self, s):
        if not s:
            return False

        pattern = re.compile(r'^[+-]?[0-9]*(\.[0-9]+)?([eE][+-]?[0-9]+)?$')
        # ^[+-]?                starts with + or -
        # [0-9]*                match .2 for example
        # (\.[0-9]+)?           match float number
        # ([eE][+-]?[0-9]+)?    match e-1 or e1
        # $                     finish matching
        res = pattern.match(s)
        if res:
            return True
        else:
            return False


if __name__ == '__main__':
    res = Solution()
    a = res.isNumeric('.45e3')
    print(a)
