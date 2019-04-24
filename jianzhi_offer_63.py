#!/usr/bin/env python

# encoding: utf-8

'''

@author: Jason Lee

@license: (C) Copyright @ Jason Lee

@contact: jiansenll@163.com

@file: jianzhi_offer_63.py

@time: 2019/4/24 12:15

@desc:

'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 返回对应节点TreeNode
    def KthNode(self, pRoot, k):
        if not pRoot:
            return None
        if k <= 0:
            return None

        num_left = self.num_node(pRoot.left)
        if num_left + 1 == k:
            return pRoot
        elif num_left + 1 > k:  # the result is in the left subtree
            return self.KthNode(pRoot.left, k)
        else:
            return self.KthNode(pRoot.right, k - num_left - 1)


    def num_node(self, pRoot):
        if not pRoot:
            return 0
        return self.num_node(pRoot.left) + self.num_node(pRoot.right) + 1