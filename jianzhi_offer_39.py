#!/usr/bin/env python

# encoding: utf-8

'''

@author: Jason Lee

@license: (C) Copyright @ Jason Lee

@contact: jiansenll@163.com

@file: jianzhi_offer_39.py

@time: 2019/5/13 14:40

@desc:

'''


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def TreeDepth(self, pRoot):
        if not pRoot:
            return 0
        depth = max(self.TreeDepth(pRoot.left), self.TreeDepth(pRoot.right)) + 1
        return depth
