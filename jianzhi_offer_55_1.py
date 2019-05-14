#!/usr/bin/env python

# encoding: utf-8

'''

@author: Jason Lee

@license: (C) Copyright @ Jason Lee

@contact: jiansenll@163.com

@file: jianzhi_offer_55_1.py

@time: 2019/5/14 14:01

@desc:

'''
class Solution:
    # 返回对应char
    def __init__(self):
        self.first = {}
        self.string = []

    def FirstAppearingOnce(self):
        # write code here
        for i in self.string:
            if self.first[i] == 0:
                return i
        # 没有只出现一次的字符
        return '#'

    def Insert(self, char):
        self.string.append(char)
        if char not in self.first.keys():
            self.first[char] = 0
        else:
            self.first[char] += 1


