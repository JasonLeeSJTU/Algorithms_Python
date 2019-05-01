#!/usr/bin/env python

# encoding: utf-8

'''

@author: Jason Lee

@license: (C) Copyright @ Jason Lee

@contact: jiansenll@163.com

@file: jianzhi_offer_35.py

@time: 2019/5/1 15:07

@desc:

'''

class Solution:
    def FirstNotRepeatingChar(self, s):
        if not s:
            return -1
        count = [0] * (ord('z') - ord('A') + 1)
        for val in s:
            count[ord(val) - ord('A')] += 1
        flag = False
        for i, val in enumerate(s):
            if count[ord(val) - ord('A')] == 1:
                flag = True
                return i
        if not flag:
            return -1

if __name__ == '__main__':
    res = Solution()
    a = res.FirstNotRepeatingChar('abcabdc')
    print(a)