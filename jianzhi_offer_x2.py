#!/usr/bin/env python

# encoding: utf-8

'''

@author: Jason Lee

@license: (C) Copyright @ Jason Lee

@contact: jiansenll@163.com

@file: jianzhi_offer_x2.py

@time: 2019/5/14 13:30

@desc:

'''


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # solution 1
    def IsBalanced_Solution(self, pRoot):
        '''@type pRoot: TreeNode'''
        if not pRoot:
            return True

        depth_left = self.depth(pRoot.left)
        depth_right = self.depth(pRoot.right)
        flag = False
        if depth_left - depth_right <= 1 and depth_left - depth_right >= -1:
            flag = True
        flag_left = self.IsBalanced_Solution(pRoot.left)
        flag_right = self.IsBalanced_Solution(pRoot.right)

        return flag and flag_left and flag_right

    def depth(self, pRoot):
        if not pRoot:
            return 0
        return 1 + max(self.depth(pRoot.left), self.depth(pRoot.right))


    # solution 2
    def better_solution(self, pRoot):
        # transverse from bottom to top
        return self.get_depth(pRoot) != -1

    def get_depth(self, pRoot):
        if not pRoot:
            return 0
        left = self.get_depth(pRoot.left)
        if left == -1:
            return -1
        right = self.get_depth(pRoot.right)
        if right == -1:
            return -1

        return -1 if abs(left - right) > 1 else 1 + max(left, right)
