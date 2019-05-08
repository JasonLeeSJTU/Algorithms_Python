#!/usr/bin/env python

# encoding: utf-8

'''

@author: Jason Lee

@license: (C) Copyright @ Jason Lee

@contact: jiansenll@163.com

@file: jianzhi_offer_42_1.py

@time: 2019/5/8 15:45

@desc:

'''
# 左旋转字符串
class Solution:
    def LeftRotateString(self, s, n):
        if not s:
            return None
        return s[n:] + s[:n]

    # 先把‘abc’和‘defg’分别翻转，得到‘cbagfed’，再反转此字符串，得到‘defgabc’
    def LeftRotateString1(self, s, n):
        if not s:
            return None
        if n == 0:
            return s
        a = s[:n]
        b = s[n:]
        a = a[::-1]
        b = b[::-1]
        c = a+b
        return c[::-1]

if __name__ == '__main__':
    res = Solution()
    a = res.LeftRotateString1("abcdefg", 3)
    print(a)