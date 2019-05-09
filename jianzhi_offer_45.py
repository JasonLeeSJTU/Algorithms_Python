#!/usr/bin/env python

# encoding: utf-8

'''

@author: Jason Lee

@license: (C) Copyright @ Jason Lee

@contact: jiansenll@163.com

@file: jianzhi_offer_45.py

@time: 2019/5/8 16:06

@desc:

'''

import sys


class Solution:
    def LastRemaining_Solution(self, n, m):
        if n == 1:
            return 0
        if m <= 0:
            return -1
        res = list(range(n))
        # 需要循环n-1次
        start = 0
        for i in range(n - 1):
            idx = (m % n + start - 1) % n
            res.pop(idx)
            start = idx
            n = n - 1
        return res[0]

    def LastRemaining_Solution1(self, n, m):
        if n == 1:
            return 0
        if m <= 0:
            return None
        self.res = list(range(n))
        self.core(n, m, 0)
        return self.res[0]

    def core(self, n, m, start):
        if n == 1:  # 只剩下最后一人
            return
        idx = (m % n + start - 1) % n  # 这个人出局
        self.res.pop(idx)
        # 从start开始计算，移动m%n步（前移m-1个）
        self.core(n - 1, m, idx)


if __name__ == '__main__':
    res = Solution()
    a = res.LastRemaining_Solution(4000, 997)
    print(a)
    # print(sys.getrecursionlimit())
