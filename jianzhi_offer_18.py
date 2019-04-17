#!/usr/bin/env python

# encoding: utf-8

'''

@author: Jason Lee

@license: (C) Copyright @ Jason Lee

@contact: jiansenll@163.com

@file: jianzhi_offer_18.py

@time: 2019/4/17 12:46

@desc:

'''


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        result = False
        if pRoot1 and pRoot2:
            # find root of tree 2 in tree 1
            if pRoot1.val == pRoot2.val:
                result = self.find_subtree(pRoot1, pRoot2)
            if not result:
                result = self.HasSubtree(pRoot1.left, pRoot2) or self.HasSubtree(pRoot1.right, pRoot2)

        return result

    def find_subtree(self, tree1, tree2):
        # three cases of results
        if not tree1 and not tree2:
            return True
        if not tree1 and tree2:
            return False
        if tree1 and not tree2:
            return True

        # if tree1 and tree2, do the following
        if tree1.val == tree2.val:
            return self.find_subtree(tree1.left, tree2.left) and self.find_subtree(tree1.right, tree2.right)
        else:
            return False
