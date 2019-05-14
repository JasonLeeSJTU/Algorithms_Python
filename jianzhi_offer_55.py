#!/usr/bin/env python

# encoding: utf-8

'''

@author: Jason Lee

@license: (C) Copyright @ Jason Lee

@contact: jiansenll@163.com

@file: jianzhi_offer_55.py

@time: 2019/5/14 14:01

@desc:

'''
class Solution:
    # 返回对应char
    def __init__(self):
        self.first = []

    def FirstAppearingOnce(self):
        # write code here
        if self.first:
            return self.first[0]
        else:
            return '#'

    # 这是一个错误的解法
    # 当googo，会输出o，出现奇数次的字符会被错误统计
    def Insert(self, char):
        if not self.first:
            self.first.append(char)
        else:
            for id, val in enumerate(self.first):
                if val == char:
                    self.first.pop(id)
                    return
            # self.first中还没有char这个字符
            self.first.append(char)


