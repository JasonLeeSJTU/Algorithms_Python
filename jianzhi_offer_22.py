#!/usr/bin/env python

# encoding: utf-8

'''

@author: Jason Lee

@license: (C) Copyright @ Jason Lee

@contact: jiansenll@163.com

@file: jianzhi_offer_22.py

@time: 2019/5/5 20:38

@desc:

'''


class Solution:
    def IsPopOrder(self, pushV, popV):
        if not pushV or not popV:
            return False
        stack = []
        for i in popV:
            while not stack or stack[-1] != i:
                if pushV:
                    temp = pushV.pop(0)
                    stack.append(temp)
                else:
                    break
            if stack[-1] == i:
                stack.pop()
            else:
                break

        if not stack and not pushV:
            return True
        else:
            return False

if __name__ == '__main__':
    push = [1,2,3,4,5]
    pop = [4,5,3,2,1]
    res = Solution()
    a = res.IsPopOrder(push, pop)
    print(a)