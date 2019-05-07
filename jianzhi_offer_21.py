#!/usr/bin/env python

# encoding: utf-8

'''

@author: Jason Lee

@license: (C) Copyright @ Jason Lee

@contact: jiansenll@163.com

@file: jianzhi_offer_21.py

@time: 2019/5/7 19:24

@desc:

'''


class Solution:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, node):
        self.stack.append(node)
        min_value = node
        if self.min_stack:
            temp = self.min_stack[-1]
            if temp < min_value:
                min_value = temp
        self.min_stack.append(min_value)

    def pop(self):
        if self.stack:
            self.stack.pop()
            self.min_stack.pop()

    def top(self):
        if self.stack:
            return self.stack[-1]
        else:
            return None

    def min(self):
        if self.min_stack:
            return self.min_stack[-1]
        else:
            return None
