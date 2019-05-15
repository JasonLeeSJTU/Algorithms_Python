#!/usr/bin/env python

# encoding: utf-8

'''

@author: Jason Lee

@license: (C) Copyright @ Jason Lee

@contact: jiansenll@163.com

@file: jianzhi_offer_47.py

@time: 2019/5/15 15:04

@desc:

'''
class Solution:
    def Add(self, num1, num2):
        # 异或：两数相加，不考虑进位
        # 与：  进位的位置（左移一位）
        while num2:
            sum = num1 ^ num2
            carry = (num1 & num2) << 1
            num1 = sum & 0xffffffff #转化为无符号二进制
            num2 = carry & 0xffffffff

        # 负数的第32位是1，正数是0
        return num1 if num1 >> 31 == 0 else ~(num1 ^ 0xffffffff) # 或者是 num1 - 0xffffffff - 1, 4294967296

if __name__ == '__main__':
    res = Solution()
    a = res.Add(111, 899)
    print(a)
