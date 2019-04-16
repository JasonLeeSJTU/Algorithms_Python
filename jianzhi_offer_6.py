#!/usr/bin/env python

# encoding: utf-8

'''

@author: Jason Lee

@license: (C) Copyright @ Jason Lee

@contact: jiansenll@163.com

@file: jianzhi_offer_6.py

@time: 2019/4/16 16:01

@desc:

'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        if not pre or not tin:
            return None
        root = TreeNode(pre[0])
        root_idx = tin.index(pre[0])
        left_tree = tin[:root_idx]
        right_tree = tin[root_idx+1:]
        root.left = self.reConstructBinaryTree(pre[1:root_idx+1], left_tree)
        root.right = self.reConstructBinaryTree(pre[root_idx+1:], right_tree)
        return root

if __name__ == '__main__':
    re = Solution()
    pre = [1,2,4,7,3,5,6,8]
    tin = [4,7,2,1,5,3,8,6]
    root = re.reConstructBinaryTree(pre, tin)
    print(root)