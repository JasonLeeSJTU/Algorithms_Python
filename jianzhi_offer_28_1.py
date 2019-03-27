#!/usr/bin/env python

# encoding: utf-8

'''

@author: Jason Lee

@license: (C) Copyright @ Jason Lee

@contact: jiansenll@163.com

@file: jianzhi_offer_28.py

@time: 2019/3/26 18:26

@desc:
字符串的排列:

输入一个字符串,按字典序打印出该字符串中字符的所有排列。
例如输入字符串abc,则打印出由字符a,b,c所能排列出来的所有字符串abc,acb,bac,bca,cab和cba。

Recursive implementation
'''


def Permutation(str):
    temp = list(str)
    res = []
    if not temp or len(temp) == 1:
        return temp
    for i in range(0, len(temp)):
        temp[0], temp[i] = temp[i], temp[0]
        temp1 = Permutation(temp[1:])
        for j in temp1:
            res.append(temp[0] + j)
        temp[0], temp[i] = temp[i], temp[0]
    return sorted(list(set(res)))



if __name__ == '__main__':
    str = "aba"
    b = Permutation(str)
    print(b)
    #print(['a'+'b',1])
