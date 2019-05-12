#!/usr/bin/env python

# encoding: utf-8

'''

@author: Jason Lee

@license: (C) Copyright @ Jason Lee

@contact: jiansenll@163.com

@file: jianzhi_offer_9.py

@time: 2019/5/12 20:12

@desc:

'''
class Solution:
    def Fibonacci(self, n):
        if n<=0:
            return 0
        if n <= 2:
            return 1

        fib = [1, 1]
        for i in range(1, n-1):
            temp = fib[i] + fib[i-1]
            fib.append(temp)
        return fib[-1]