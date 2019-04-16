#!/usr/bin/env python

# encoding: utf-8

'''

@author: Jason Lee

@license: (C) Copyright @ Jason Lee

@contact: jiansenll@163.com

@file: jianzhi_offer_67.py

@time: 2019/4/16 13:13

@desc:

'''

class Solution:
    def movingCount(self, threshold, rows, cols):
        covered = [[0]*cols for i in range(rows)]
        count = 0
        count = self.movingCountCore(threshold, 0, 0, covered, count, rows, cols)
        return count

    def movingCountCore(self, threshold, row, col, covered, count, rows, cols):
        if row < 0 or row >= rows or col < 0 or col >= cols:
            return count
        if self.calc_number(row) + self.calc_number(col) > threshold:
            return count
        if covered[row][col] > 0:
            return count
        covered[row][col] = 1
        count += 1
        # up
        count = self.movingCountCore(threshold, row-1, col, covered, count, rows, cols)
        # down
        count = self.movingCountCore(threshold, row+1, col, covered, count, rows, cols)
        # left
        count = self.movingCountCore(threshold, row, col-1, covered, count, rows, cols)
        # right
        count = self.movingCountCore(threshold, row, col+1, covered, count, rows, cols)
        return count


    def calc_number(self, num):
        a = [int(x) for x in str(num)]
        return sum(a)


if __name__ == '__main__':
    res = Solution()
    a = res.movingCount(5, 10, 10)
    print(a)