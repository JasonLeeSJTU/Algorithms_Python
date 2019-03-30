#!/usr/bin/env python

# encoding: utf-8

'''

@author: Jason Lee

@license: (C) Copyright @ Jason Lee

@contact: jiansenll@163.com

@file: jianzhi_offer_62.py

@time: 2019/3/30 10:30

@desc:

'''

import collections


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.id = -1

    def Serialize(self, root):
        def flatten(lst):
            for item in lst:
                if isinstance(item, collections.Iterable) and not isinstance(item, (str, bytes)):
                    yield from flatten(item)
                else:
                    yield item

        res = self.Serialize_core(root)
        return list(flatten(res))

    def Serialize_core(self, root):
        if not root:
            return '$'

        return [root.val, self.Serialize_core(root.left), self.Serialize_core(root.right)]

    def Serialize1(self, root):
        if not root:
            return '$,'
        return str(root.val) + ',' + self.Serialize1(root.left) + self.Serialize1(root.right)

    def Deserialize(self, s):
        l = s.split(',')
        self.id += 1
        if self.id >= len(l):
            return None

        head = None
        if l[self.id] != '$':
            head = TreeNode(int(l[self.id]))
            head.left = self.Deserialize(s)
            head.right = self.Deserialize(s)
        return head


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    left = root.left
    left.left = TreeNode(4)
    right = root.right
    right.left = TreeNode(5)
    right.right = TreeNode(6)
    so = Solution()
    str = so.Serialize1(root)
    print(str)
    head = so.Deserialize(str)
    print(head)
