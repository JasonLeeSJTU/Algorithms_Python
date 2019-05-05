#!/usr/bin/env python

# encoding: utf-8

'''

@author: Jason Lee

@license: (C) Copyright @ Jason Lee

@contact: jiansenll@163.com

@file: jianzhi_offer_51.py

@time: 2019/5/5 20:19

@desc:

'''
class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self, numbers, duplication):
        if not numbers:
            return False
        array = {}
        for i in numbers:
            if str(i) not in array.keys():
                array[str(i)] = 1
            else:
                # this number is duplicated
                duplication[0] = i
                return True
                #array[str(i)] += 1
        return False