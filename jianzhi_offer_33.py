#!/usr/bin/env python

# encoding: utf-8

'''

@author: Jason Lee

@license: (C) Copyright @ Jason Lee

@contact: jiansenll@163.com

@file: jianzhi_offer_33.py

@time: 2019/5/3 16:15

@desc:

'''
class Solution:
    def PrintMinNumber(self, numbers):
        temp = []
        max_len = 0
        for i in numbers:
            temp_list = list(str(i))
            temp.append(temp_list)
            max_len = len(temp_list) if max_len < len(temp_list) else max_len

        # extend all numbers to length max_len
        # use the last integer to fill the extended positions
        temp_full = []
        for i in temp:
            current_number = i
            for j in range(max_len - len(i)):
                current_number.append(i[-1])
            temp_full.append(int(''.join(current_number)))

        # sort and return the index
        index = sorted(range(len(temp_full)), key=lambda c: temp_full[c])

        # concatenate numbers according to index
        temp_index = []
        for i in index:
            temp_index.append(str(numbers[i]))

        return int(''.join(temp_index))


if __name__ == '__main__':
    a = [332, 321]
    res = Solution()
    b = res.PrintMinNumber(a)
    print(b)
