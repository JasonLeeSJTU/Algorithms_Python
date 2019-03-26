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

'''


def Permutation(str):
    #temp = list(set(str))  # filter out the duplicate character
    temp = list(str)
    if not temp:
        return temp
    if len(temp) == 1:
        return temp

    i = -2
    res = temp[-1]
    while i >= -len(temp):
        res = combine(temp[i], res)
        i -= 1

    #return sorted(set(res), key=res.index)
    return sorted(set(res))


def combine(a, b):  # insert character a into string b
    # character a will be inserted into b with len(b)+1 times
    res = []
    for bb in b:
        i = 0
        while i <= len(bb):
            res.append(''.join([bb[:i], a, bb[i:]]))
            i += 1
    return res


if __name__ == '__main__':
    str = "abc"
    b = Permutation(str)
    print(b)
