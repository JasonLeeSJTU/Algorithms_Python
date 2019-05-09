#!/usr/bin/env python

# encoding: utf-8

'''

@author: Jason Lee

@license: (C) Copyright @ Jason Lee

@contact: jiansenll@163.com

@file: jianzhi_offer_58.py

@time: 2019/5/9 12:58

@desc:

'''


class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None


class Solution:
    def GetNext(self, pNode):
        if not pNode:
            return None
        if pNode.right:
            node = pNode.right
            while node.left:
                node = node.left
            return node
        else:
            if pNode.next:
                node = pNode.next
                if pNode == node.left:  # left child, then return father node
                    return node
                else:   # right child
                    if node.next:
                        node_father = node.next
                        if node == node_father.left: # left child, then return this father node
                            return node_father
                        else:   # right child, 要一直向上找，直到一个节点是父节点的左节点
                            while node_father.next:
                                if node_father == node_father.next.left:
                                    return node_father.next
                                else:
                                    node_father = node_father.next
                            return node_father.next
            else:
                return None
