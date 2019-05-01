#!/usr/bin/env python

# encoding: utf-8

'''

@author: Jason Lee

@license: (C) Copyright @ Jason Lee

@contact: jiansenll@163.com

@file: jianzhi_offer_35_1.py

@time: 2019/5/1 15:48

@desc:

'''

class Solution:
    def FirstNotRepeatingChar(self, s):
        if not s:
            return -1
        count = {}
        for val in s:
            if val not in count.keys():
                count[val] = 0
            count[val] += 1

        for val in s:
            if count[val] == 1:
                return s.index(val)

        return -1

if __name__ == '__main__':
    res = Solution()
    a = res.FirstNotRepeatingChar('abcabdcd')
    print(a)