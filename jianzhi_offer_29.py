#!/usr/bin/env python

# encoding: utf-8

'''

@author: Jason Lee

@license: (C) Copyright @ Jason Lee

@contact: jiansenll@163.com

@file: jianzhi_offer_29.py

@time: 2019/5/4 15:28

@desc:

'''
import random
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        if not numbers:
            return 0

        middle = len(numbers) // 2
        idx = self.partition(numbers, 0, len(numbers)-1)
        start = 0
        end = len(numbers) - 1
        while idx != middle:
            while idx < middle:
                start = idx + 1
                idx = self.partition(numbers, start, end)
            while idx > middle:
                end = idx - 1
                idx = self.partition(numbers, start, end)

        # check if exists this number
        num = numbers[idx]
        count = 0
        for i in numbers:
            if i == num:
                count += 1

        if count <= middle: # because middle counts from 0
            return 0
        else:
            return num

    # randomly select a number, put all data that are smaller than this number in front
    # put all data that are bigger than this number at the last
    # return the final position of this number
    def partition(self, array, start, end):
        if start == end:
           return start
        id = random.randint(start, end)
        # move this number to index 0
        array[start], array[id] = array[id], array[start]
        left = start + 1
        right = end
        while True:
            while array[left] <= array[start] and left < end:
                left += 1
            while array[right] > array[start] and right > start:
                right -= 1
            if left >= right:
                break
            array[left], array[right] = array[right], array[left]

        array[start], array[right] = array[right], array[start]
        return right

if __name__ == '__main__':
    res = Solution()
    ar = [1,3,4,5,2,2,2,2,2]
    a = res.MoreThanHalfNum_Solution(ar)
    print(a)