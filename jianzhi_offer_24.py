#!/usr/bin/env python

# encoding: utf-8

'''

@author: Jason Lee

@license: (C) Copyright @ Jason Lee

@contact: jiansenll@163.com

@file: jianzhi_offer_24.py

@time: 2019/4/18 10:12

@desc:

'''


class Solution:
    def VerifySquenceOfBST(self, sequence):
        if not sequence:
            return False
        return self.verify(sequence)

    def verify(self, sequence):
        if len(sequence) == 1:
            return True

        root = sequence[-1]  # root node
        flag = False  # find an item larger than root?
        split = len(sequence) - 2  # second to last
        for idx, val in enumerate(sequence):
            if not flag and val > root:
                split = idx - 1
                flag = True
            if flag and val < root:
                return False
        if split < 0:   # split = -1, all items are larger than root
            split = 0

        return self.verify(sequence[:split + 1]) and self.verify(sequence[split:-1])


if __name__ == '__main__':
    res = Solution()
    a = res.VerifySquenceOfBST([5, 4, 3, 2, 1])
    print(a)
