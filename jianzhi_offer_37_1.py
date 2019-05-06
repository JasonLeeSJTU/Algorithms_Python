#!/usr/bin/env python

# encoding: utf-8

'''

@author: Jason Lee

@license: (C) Copyright @ Jason Lee

@contact: jiansenll@163.com

@file: jianzhi_offer_37_1.py

@time: 2019/5/6 16:46

@desc:

'''


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        if not pHead1 or not pHead2:
            return None
        node1 = pHead1
        node2 = pHead2
        while node1 != node2:   # None == None, exit while loop
            node1 = pHead2 if not node1 else node1.next
            node2 = pHead1 if not node2 else node2.next

        return node1
