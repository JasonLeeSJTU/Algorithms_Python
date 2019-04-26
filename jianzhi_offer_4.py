#!/usr/bin/env python

# encoding: utf-8

'''

@author: Jason Lee

@license: (C) Copyright @ Jason Lee

@contact: jiansenll@163.com

@file: jianzhi_offer_4.py

@time: 2019/4/26 16:22

@desc:

'''
class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        temp = list(s)
        for i, val in enumerate(temp):
            if val == " ":
                temp[i] = "%20"
        return ''.join(temp)

if __name__ == '__main__':
    res = Solution()
    str = "hello  world"
    a = res.replaceSpace(str)
    print(a)

