#!/usr/bin/env python

# encoding: utf-8

'''

@author: Jason Lee

@license: (C) Copyright @ Jason Lee

@contact: jiansenll@163.com

@file: jianzhi_offer_56.py

@time: 2019/5/14 15:18

@desc:

'''


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def EntryNodeOfLoop(self, pHead):
        if not pHead:
            return None

        # 判断是否包含环
        p1 = pHead
        # 只有一个节点时，不存在环
        if not pHead.next:
            return None
        p2 = pHead.next

        while p1 and p2 and p1 != p2:
            p1 = p1.next
            p2 = p2.next.next
        if not p1 or not p2:
            return None # 不存在环

        # 将p1指向链表开头，与p2每次移动一个节点，两者再次相遇，就是环的入口
        p1 = pHead
        p2 = p2.next
        while p1 != p2:
            p1 = p1.next
            p2 = p2.next

        return p1

if __name__ == '__main__':
    root = ListNode(1)
    root.next = ListNode(2)
    root.next.next = ListNode(3)
    root.next.next.next = root
    res = Solution()
    a = res.EntryNodeOfLoop(root)
    print(a.val)