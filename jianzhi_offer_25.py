#!/usr/bin/env python

# encoding: utf-8

'''

@author: Jason Lee

@license: (C) Copyright @ Jason Lee

@contact: jiansenll@163.com

@file: jianzhi_offer_25.py

@time: 2019/5/1 16:01

@desc:

'''


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def __init__(self):
        self.res = []

    def FindPath(self, root, expectNumber):
        if not root:
            return []
        if root.val > expectNumber:
            return []
        if root.val == expectNumber:
            return [[root.val]]     # two [], because the result is in this form [[1,2,3], [3,3]]
        path = []
        currentSum = 0
        self.find_path_core(root, expectNumber, path, currentSum)

        return sorted(self.res, key=lambda c: len(c), reverse=True)


    def find_path_core(self, root, expectNumber, path, currentSum):
        # @type root: TreeNode
        currentSum += root.val
        path.append(root)
        if not root.left and not root.right:    # reach leaf node
            if currentSum == expectNumber:
                temp = []
                for i in path:
                    temp.append(i.val)
                self.res.append(temp)   # record this path

        # not leaf node
        if root.left:
            self.find_path_core(root.left, expectNumber, path, currentSum)
        if root.right:
            self.find_path_core(root.right, expectNumber, path, currentSum)

        path.pop()  # delete current node


if __name__ == '__main__':
    res = Solution()
    root = TreeNode(1)
    root.left = TreeNode(6)
    root.right = TreeNode(3)
    #root.left.left = TreeNode(4)
    #root.left.right = TreeNode(5)
    root.right.left = TreeNode(3)
    root.right.right = TreeNode(3)

    a = res.FindPath(root, 7)
    print(a)