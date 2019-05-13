#!/usr/bin/env python

# encoding: utf-8

'''

@author: Jason Lee

@license: (C) Copyright @ Jason Lee

@contact: jiansenll@163.com

@file: jianzhi_offer_38.py

@time: 2019/5/13 12:58

@desc:

'''
class Solution:
    def GetNumberOfK(self, data, k):
        if not data:
            return 0
        count = 0
        start = self.binarySearchStart(data, 0, len(data) - 1, k)
        if start == -1:
            return 0
        end = self.binarySearchEnd(data, start, len(data) - 1, k)
        return end - start + 1

    def binarySearchStart(self, data, start, end, k):
        while start <= end:
            mid = (start + end) // 2
            if data[mid] > k:
                end = mid - 1
            elif data[mid] < k:
                start = mid + 1
            else:
                if mid > 0 and data[mid-1] != k:
                    return mid
                if mid == 0:
                    return mid
                else:
                    end = mid - 1
        return -1

    def binarySearchEnd(self, data, start, end, k):
        while start <= end:
            mid = (start + end) // 2
            if data[mid] > k:
                end = mid - 1
            elif data[mid] < k:
                start = mid + 1
            else:
                if mid < len(data) - 1 and data[mid + 1] != k:
                    return mid
                if mid == len(data) - 1:
                    return mid
                else:
                    start = start + 1
        return -1

if __name__ == '__main__':
    res = Solution()
    a = [1,1,1,2]
    b = res.GetNumberOfK(a, 2)
    print(b)