#!/usr/bin/env python

# encoding: utf-8

'''

@author: Jason Lee

@license: (C) Copyright @ Jason Lee

@contact: jiansenll@163.com

@file: jianzhi_offer_8.py

@time: 2019/5/15 15:38

@desc:

'''


class Solution:
    def minNumberInRotateArray(self, rotateArray):
        if not rotateArray:
            return 0
        if len(rotateArray) == 1:
            return rotateArray[0]

        left = 0
        right = len(rotateArray) - 1
        if rotateArray[left] < rotateArray[right]:  # 没有旋转
            return rotateArray[left]

        mid = (left + right) >> 1
        while mid != left:
            if rotateArray[left] < rotateArray[right]:
                return rotateArray[left]

            if rotateArray[mid] > rotateArray[left] or rotateArray[mid] > rotateArray[right]:
                left = mid
            elif rotateArray[mid] < rotateArray[right]:
                right = mid
            else:
                # 三者相等，用顺序查找法
                for i in range(len(rotateArray)-2, -1, -1):
                    if rotateArray[i] > rotateArray[i+1]:
                        return rotateArray[i+1]

            mid = (left + right) >> 1

        return rotateArray[right]

if __name__ == '__main__':
    a = [1,1,1,0,1]
    res = Solution()
    b = res.minNumberInRotateArray(a)
    print(b)