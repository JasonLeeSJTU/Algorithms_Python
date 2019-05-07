#!/usr/bin/env python

# encoding: utf-8

'''

@author: Jason Lee

@license: (C) Copyright @ Jason Lee

@contact: jiansenll@163.com

@file: jianzhi_offer_16.py

@time: 2019/5/7 13:57

@desc:

'''


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 返回ListNode
    def ReverseList1(self, pHead):
        if not pHead:
            return None
        stack = []
        while pHead:
            stack.append(pHead)
            pHead = pHead.next

        head = stack.pop()
        temp = head
        while stack:
            temp.next = stack.pop()
            temp = temp.next
        temp.next = None    ### Important !!!!! otherwise, the result will be a circle

        return head

    # better solution
    def ReverseList(self, pHead):
        # use two pointers to reverse the list
        if not pHead:
            return None
        pre = None
        while pHead:
            cur = pHead.next
            pHead.next = pre
            pre = pHead
            pHead = cur
        return pre

if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(3)
    head.next.next = ListNode(4)
    res = Solution()
    a = res.ReverseList(head)

    while a:
        print(a.val)
        a = a.next