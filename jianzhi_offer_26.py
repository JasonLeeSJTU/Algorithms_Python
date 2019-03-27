#!/usr/bin/env python

# encoding: utf-8

'''

@author: Jason Lee

@license: (C) Copyright @ Jason Lee

@contact: jiansenll@163.com

@file: jianzhi_offer_26.py

@time: 2019/3/27 22:47

@desc:

'''
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

def Clone(pHead):
    if not pHead:
        return None

    dummy = pHead
    while dummy:
        dummy_next = dummy.next
        node = RandomListNode(dummy.label)
        node.next = dummy.next
        dummy.next = node
        dummy = dummy_next

    dummy = pHead
    while dummy:
        node = dummy.next
        temp = dummy.random
        if temp:
            node.random = temp.next
        dummy = node.next

    # split the list to two
    res = pHead.next
    dummy = pHead
    while dummy:
        node = dummy.next
        if node.next:
            dummy.next = node.next
            dummy = dummy.next
            node.next = dummy.next
            node = node.next
        else:
            dummy.next = None
            node.next = None
            dummy = dummy.next
            node = node.next

    return res

