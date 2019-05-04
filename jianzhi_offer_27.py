#!/usr/bin/env python

# encoding: utf-8

'''

@author: Jason Lee

@license: (C) Copyright @ Jason Lee

@contact: jiansenll@163.com

@file: jianzhi_offer_27.py

@time: 2019/5/4 16:57

@desc:

'''


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.res = None
        self.root = None

    def Convert(self, pRootOfTree):
        if not pRootOfTree:
            return
        # mid-transverse of the binary search tree
        self.transverse(pRootOfTree)
        # here self.root is a one-side linked list using the left pointer

        # add right pointer to self.root
        father = self.root
        child = father.left
        while child:
            child.right = father
            father = child
            child = father.left

        return self.root

    def transverse(self, root):
        if root.left:
            self.transverse(root.left)
        if not self.res:
            self.res = root
            self.root = root
        else:
            self.res.left = root
            self.res = self.res.left
        if root.right:
            self.transverse(root.right)

if __name__ == '__main__':
    root = TreeNode(10)
    root.left = TreeNode(6)
    root.right = TreeNode(14)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(8)
    root.right.left = TreeNode(12)
    root.right.right = TreeNode(16)

    res = Solution()
    a = res.Convert(root)

    while a:
        print(a.val)
        b = a
        a = a.left
    print('\n')
    while b:
        print(b.val)
        b = b.right