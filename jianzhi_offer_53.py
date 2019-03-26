#!/usr/bin/env python

# encoding: utf-8

'''

@author: Jason Lee

@license: (C) Copyright @ Jason Lee

@contact: jiansenll@163.com

@file: jianzhi_offer_53.py

@time: 2019/3/26 9:50

@desc:
正则表达式匹配:

请实现一个函数用来匹配包括'.'和'*'的正则表达式。模式中的字符'.'表示任意一个字符，
而'*'表示它前面的字符可以出现任意次（包含0次）。 在本题中，匹配是指字符串的所有字符匹配整个模式。
例如，字符串"aaa"与模式"a.a"和"ab*ac*a"匹配，但是与"aa.a"和"ab*a"均不匹配
'''


# string = "aaa", str = "a.a"
def match(s, pattern):
    if not s and not pattern:
        return True
    if not pattern and s:
        return False
    if not s and pattern:
        if len(pattern) > 1 and pattern[1] == '*':
            return match(s, pattern[2:])
        else:
            return False

    # both s and pattern are not empty
    if len(pattern) > 1 and pattern[1] == '*':
        if pattern[0] != s[0] and pattern[0] != '.':
            return match(s, pattern[2:])
        else:
            return match(s, pattern[2:]) or match(s[1:], pattern)
    elif pattern[0] == s[0] or pattern[0] == '.':
        return match(s[1:], pattern[1:])


if __name__ == '__main__':
    # string = "aaa"
    string = "abbcde"
    # str = "a*"
    str = ".*"
    # str = "a.a"
    # str = "ab*ac*a"
    # str = "aa.a"
    # str = "ab*a"
    res = match(string, str)
    print(res)
