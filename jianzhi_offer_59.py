#!/usr/bin/env python

# encoding: utf-8

'''

@author: Jason Lee

@license: (C) Copyright @ Jason Lee

@contact: jiansenll@163.com

@file: jianzhi_offer_59.py

@time: 2019/5/9 13:23

@desc:

'''


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetrical(self, pRoot):
        if not pRoot:
            return False
        if not pRoot.left and pRoot.right:
            return False
        if pRoot.left and not pRoot.right:
            return False
        if not pRoot.left and not pRoot.right:
            return True

        # compare left tree and right tree
        return self.compare(pRoot.left, pRoot.right)

    def compare(self, left, right):
        if left.val != right.val:
            return False
        flag_left = False
        flag_right = False
        if left.left and right.right:
            flag_left = self.compare(left.left, right.right)
        elif not left.left and not right.right:
            flag_left = True
        if left.right and right.left:
            flag_right = self.compare(left.right, right.left)
        elif not left.right and not right.left:
            flag_right = True

        return flag_left and flag_right
