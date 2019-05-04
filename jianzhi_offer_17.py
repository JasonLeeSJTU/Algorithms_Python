#!/usr/bin/env python

# encoding: utf-8

'''

@author: Jason Lee

@license: (C) Copyright @ Jason Lee

@contact: jiansenll@163.com

@file: jianzhi_offer_17.py

@time: 2019/5/4 14:36

@desc:

'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        '''@type pHead1: ListNode
        @type pHead2: ListNode'''
        if not pHead1:
            return pHead2
        if not pHead2:
            return pHead1

        root = None
        if pHead1.val <= pHead2.val:
            root = pHead1
            pHead1 = pHead1.next
        else:
            root = pHead2
            pHead2 = pHead2.next

        res = root
        while pHead1 and pHead2:
            if pHead1.val <= pHead2.val:
                res.next = pHead1
                pHead1 = pHead1.next
            else:
                res.next = pHead2
                pHead2 = pHead2.next
            res = res.next

        if pHead1:
            res.next = pHead1
        if pHead2:
            res.next = pHead2

        return root