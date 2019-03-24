#!/usr/bin/env python

# encoding: utf-8

'''

@author: Jason Lee

@license: (C) Copyright @ Jason Lee

@contact: jiansenll@163.com

@file: jianzhi_offer_36.py

@time: 2019/3/24 21:39

@desc:

题目描述:

在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。
输入一个数组,求出这个数组中的逆序对的总数P。并将P对1000000007取模的结果输出。
即输出P%1000000007


'''
def inverse_pairs(data):
    count, temp = count_sort(data)
    return count % 1000000007

def count_sort(data):
    if len(data) <= 1:
        return 0, data

    mid = len(data) // 2

    count_left, left = count_sort(data[:mid])
    count_right, right = count_sort(data[mid:])

    count_two, temp_data = count_merge(left, right)
    return count_left + count_right + count_two, temp_data


def count_merge(left, right):
    temp = []
    i = 0
    j = 0
    count = 0
    while i < len(left) and j < len(right):
        if left[i] > right[j]:
            count += len(left) - i
            temp.append(right[j])
            j += 1
        else:
            temp.append(left[i])
            i += 1

    while i < len(left):
        temp.append(left[i])
        i = i + 1

    while j < len(right):
        temp.append(right[j])
        j = j + 1

    return count, temp


if __name__ == '__main__':
    a = [1,2,3,4,5,6,7,0]
    count = inverse_pairs(a)
    print(count)
