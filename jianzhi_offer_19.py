#!/usr/bin/env python

# encoding: utf-8

'''

@author: Jason Lee

@license: (C) Copyright @ Jason Lee

@contact: jiansenll@163.com

@file: jianzhi_offer_19.py

@time: 2019/5/7 15:06

@desc:

'''


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回镜像树的根节点
    def Mirror(self, root):
        if not root:
            return
        left = root.left
        right = root.right
        root.left = right
        root.right = left
        self.Mirror(root.left)
        self.Mirror(root.right)
