#!/usr/bin/env python

# encoding: utf-8

'''

@author: Jason Lee

@license: (C) Copyright @ Jason Lee

@contact: jiansenll@163.com

@file: jianzhi_offer_63_2.py

@time: 2019/4/24 15:13

@desc:

'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 返回对应节点TreeNode
    # only need to inorder traversal the tree
    def KthNode(self, pRoot, k):
        if not pRoot:
            return None
        if k <= 0:
            return None
        self.k = k
        return self.inorder(pRoot)


    def inorder(self, pRoot):
        if not pRoot:   # reach a leaf node
            return None
        res = self.inorder(pRoot.left)
        if not res:
            if self.k > 1:
                self.k -= 1
                res = None
            elif self.k == 1:
                res = pRoot

        if not res:
            res = self.inorder(pRoot.right)
        return res

if __name__ == '__main__':
    root = TreeNode(8)
    left = TreeNode(6)
    right = TreeNode(10)
    left.left = TreeNode(5)
    left.right = TreeNode(7)
    right.left = TreeNode(9)
    right.right = TreeNode(11)
    root.left = left
    root.right = right
    res = Solution()
    b = res.KthNode(root, 4)
    print(b)