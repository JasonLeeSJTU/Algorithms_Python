#!/usr/bin/env python

# encoding: utf-8

'''

@author: Jason Lee

@license: (C) Copyright @ Jason Lee

@contact: jiansenll@163.com

@file: jianzhi_offer_37.py

@time: 2019/5/6 16:23

@desc:

'''


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        # store node in two stack
        # transverse from the end of the two linked list
        if not pHead1 or not pHead2:
            return None

        stack1 = []
        stack2 = []
        while pHead1:
            stack1.append(pHead1)
            pHead1 = pHead1.next
        while pHead2:
            stack2.append(pHead2)
            pHead2 = pHead2.next

        # transverse from the end, ie. the top of the two stacks
        # find the last same nodes
        node1 = stack1.pop()
        node2 = stack2.pop()
        flag = False
        while node1.val == node2.val:
            flag = True # the common node must exist
            if stack1 and stack2:
                node1 = stack1.pop()
                node2 = stack2.pop()
            else:
                return node1 # in this case, one stack is a subset of the other one

        if flag:
            return node1.next
        else:
            return None