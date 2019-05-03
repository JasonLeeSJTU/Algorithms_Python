#!/usr/bin/env python

# encoding: utf-8

'''

@author: Jason Lee

@license: (C) Copyright @ Jason Lee

@contact: jiansenll@163.com

@file: jianzhi_offer_23.py

@time: 2019/5/3 15:54

@desc:

'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        '''@type root: TreeNode'''
        if not root:
            return []
        res = [root.val]
        que =[root]
        while que:
            node = que.pop(0)
            if node.left:
                res.append(node.left.val)
                que.append(node.left)
            if node.right:
                res.append(node.right.val)
                que.append(node.right)
        return res