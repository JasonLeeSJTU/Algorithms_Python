#!/usr/bin/env python

# encoding: utf-8

'''

@author: Jason Lee

@license: (C) Copyright @ Jason Lee

@contact: jiansenll@163.com

@file: jianzhi_offer_57.py

@time: 2019/3/25 23:57

@desc:
删除链表中重复的结点:

在一个排序的链表中，存在重复的结点，请删除该链表中重复的结点，重复的结点不保留，
返回链表头指针。 例如，链表1->2->3->3->4->4->5 处理后为 1->2->5
'''
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None


def deleteDuplication(pHead):
    if not pHead or not pHead.next:
        return pHead

    if pHead.val == pHead.next.val:
        temp = pHead.next.next
        while temp and temp.val == pHead.val:   # while temp must be verified first, in case it points to the end
            temp = temp.next
        return deleteDuplication(temp)
    else:
        pHead.next = deleteDuplication(pHead.next)
        return pHead
