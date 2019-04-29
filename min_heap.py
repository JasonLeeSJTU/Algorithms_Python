#!/usr/bin/env python

# encoding: utf-8

'''

@author: Jason Lee

@license: (C) Copyright @ Jason Lee

@contact: jiansenll@163.com

@file: min_heap.py

@time: 2019/4/29 20:23

@desc:

'''


# please see the comments in max_heap.py

def min_heap(array):
    if not array:
        return None
    length = len(array)
    if length == 1:
        return array

    for i in range(length // 2 - 1, -1, -1):
        current_idx = i
        temp = array[current_idx]
        flag = False
        while not flag and 2 * current_idx + 1 < length:
            left_idx = 2 * current_idx + 1
            idx = left_idx
            if left_idx + 1 < length and array[left_idx] > array[left_idx + 1]:
                idx = left_idx + 1
            if temp > array[idx]:
                array[current_idx] = array[idx]
                current_idx = idx
            else:
                flag = True
        array[current_idx] = temp

if __name__ == '__main__':
    array = [7,6,5,4,3,2,1]
    min_heap(array)
    print(array)
