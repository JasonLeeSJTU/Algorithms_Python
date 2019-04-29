#!/usr/bin/env python

# encoding: utf-8

'''

@author: Jason Lee

@license: (C) Copyright @ Jason Lee

@contact: jiansenll@163.com

@file: max_heap.py

@time: 2019/4/29 19:58

@desc:
change a given array to max heap
'''

def max_heap(array):
    if not array:
        return None
    length = len(array)
    if length == 1:
        return array

    for i in range(length//2-1, -1, -1):    # start from the last non-leaf node
        current_idx = i
        temp = array[current_idx]
        flag = False
        while not flag and 2*current_idx+1 < length:     # while the current node has left child
            left_idx = 2*current_idx + 1
            idx = left_idx
            if left_idx+1 < length and array[left_idx] < array[left_idx + 1]:   # if left child < right child
                idx = left_idx + 1
            if temp < array[idx]:   # need to swap the value
                array[current_idx] = array[idx]
                current_idx = idx
            else:
                flag = True
        array[current_idx] = temp

if __name__ == '__main__':
    array = [79,66,43,83,30,87,38,55,91,72,49,9]
    max_heap(array)
    print(array)