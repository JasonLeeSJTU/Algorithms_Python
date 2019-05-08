#!/usr/bin/env python

# encoding: utf-8

'''

@author: Jason Lee

@license: (C) Copyright @ Jason Lee

@contact: jiansenll@163.com

@file: jianzhi_offer_40.py

@time: 2019/5/8 14:52

@desc:

'''
class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        if not array:
            return []
        stack = {}
        for i in array:
            if str(i) not in stack.keys():
                stack[str(i)] = 1
            else:
                stack[str(i)] += 1
        res = []
        for i in stack:
            if stack[i] == 1:
                res.append(int(i))
        return res

if __name__ == '__main__':
    array = [1,2,2,3]
    res = Solution()
    a = res.FindNumsAppearOnce(array)
    print(a)
