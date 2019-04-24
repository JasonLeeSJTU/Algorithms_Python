#!/usr/bin/env python

# encoding: utf-8

'''

@author: Jason Lee

@license: (C) Copyright @ Jason Lee

@contact: jiansenll@163.com

@file: jianzhi_offer_63_1.py

@time: 2019/4/24 12:57

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

        self.order = []
        self.inorder_traversal(pRoot)
        if k > len(self.order):
            return None
        return self.order[k-1]

    def inorder_traversal(self, pRoot):
        if pRoot:
            self.inorder_traversal(pRoot.left)
            self.order.append(pRoot.val)
            self.inorder_traversal(pRoot.right)


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
    b = res.KthNode(root, 1)
    print(b)