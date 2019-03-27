#!/usr/bin/env python

# encoding: utf-8

'''

@author: Jason Lee

@license: (C) Copyright @ Jason Lee

@contact: jiansenll@163.com

@file: jianzhi_offer_15.py

@time: 2019/3/27 22:06

@desc:
链表中倒数第k个结点:

输入一个链表，输出该链表中倒数第k个结点。

Traverse the linked list only once
'''
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def FindKthToTail(head, k):
    if not head or k <= 0:
        return None
    a = head
    b = head
    for i in range(k):
        if a:
            a = a.next
        else:
            return None

    while a:
        a = a.next
        b = b.next

    return b.val

if __name__ == '__main__':
    head = ListNode(1)
    dummy = head
    dummy.next = ListNode(2)
    dummy = dummy.next
    dummy.next = ListNode(3)
    print(FindKthToTail(head, 3))