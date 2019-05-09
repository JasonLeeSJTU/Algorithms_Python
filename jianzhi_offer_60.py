#!/usr/bin/env python

# encoding: utf-8

'''

@author: Jason Lee

@license: (C) Copyright @ Jason Lee

@contact: jiansenll@163.com

@file: jianzhi_offer_60.py

@time: 2019/5/9 13:54

@desc:

'''


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回二维列表[[1,2],[4,5]]
    def Print(self, pRoot):
        if not pRoot:
            return []
        res = []
        temp = [pRoot.val]
        res.append(temp)
        stack = []
        stack.append(pRoot.left)
        stack.append(pRoot.right)
        layer = []
        temp = []
        while stack or layer:
            node = stack.pop(0)
            if node:
                temp.append(node.val)
                layer.append(node.left)
                layer.append(node.right)
            if not stack:
                stack = layer
                if temp:
                    res.append(temp)
                temp = []
                layer = []

        return res
