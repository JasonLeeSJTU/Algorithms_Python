#!/usr/bin/env python

# encoding: utf-8

'''

@author: Jason Lee

@license: (C) Copyright @ Jason Lee

@contact: jiansenll@163.com

@file: jianzhi_offer_61.py

@time: 2019/4/17 14:04

@desc:

'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# use stack to store nodes
class Solution:
    def Print(self, pRoot): # @type pRoot: TreeNode
        if not pRoot:
            return []
        stack_left = []
        stack_right = []
        result = []
        # print(pRoot.val)
        result.append([pRoot.val])
        if pRoot.left:
            stack_left.append(pRoot.left)
        if pRoot.right:
            stack_left.append(pRoot.right)

        while stack_left or stack_right:
            temp = []
            while stack_left:
                node = stack_left.pop() # type: TreeNode
                # print(node.val)
                temp.append(node.val)
                if node.right:
                    stack_right.append(node.right)
                if node.left:
                    stack_right.append(node.left)
            if temp:
                result.append(temp)

            temp = []
            while stack_right:
                node = stack_right.pop()    # type: TreeNode
                # print(node.val)
                temp.append(node.val)
                if node.left:
                    stack_left.append(node.left)
                if node.right:
                    stack_left.append(node.right)
            if temp:
                result.append(temp)

        return result


if __name__ == '__main__':
    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)
    n4 = TreeNode(4)
    n5 = TreeNode(5)
    n6 = TreeNode(6)
    n7 = TreeNode(7)
    n8 = TreeNode(8)
    n9 = TreeNode(9)
    n1.left = n2
    n1.right = n3
    n2.left = n4
    n2.right = n5
    n3.left = n6
    n3.right = n7
    n4.left = n8
    n4.right = n9

    res = Solution()
    x = res.Print(n1)
    print(x)