#!/usr/bin/env python

# encoding: utf-8

'''

@author: Jason Lee

@license: (C) Copyright @ Jason Lee

@contact: jiansenll@163.com

@file: jianzhi_offer_7.py

@time: 2019/5/15 15:31

@desc:

'''


class Solution:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, node):
        # 如果stack2不为空，需要先把stack2中元素压入stack1中
        while self.stack2:
            temp = self.stack2.pop()
            self.stack1.append(temp)

        self.stack1.append(node)

    def pop(self):
        # 如果stack2不为空，直接弹出即可；如果为空，则把stack1中元素压入stack2，再弹出
        if self.stack2:
            return self.stack2.pop()
        else:
            while self.stack1:
                temp = self.stack1.pop()
                self.stack2.append(temp)

            return self.stack2.pop()