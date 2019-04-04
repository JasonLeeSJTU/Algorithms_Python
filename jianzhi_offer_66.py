#!/usr/bin/env python

# encoding: utf-8

'''

@author: Jason Lee

@license: (C) Copyright @ Jason Lee

@contact: jiansenll@163.com

@file: jianzhi_offer_66.py

@time: 2019/4/4 16:31

@desc:

'''

class Solution:
    def hasPath(self, matrix, rows, cols, path):
        if not matrix or not path:
            return False

        visited = [[0]*cols for i in range(rows)]
        id = 0

        for i in range(rows):
            for j in range(cols):
                res = self.hasPathCore(matrix, i, j, path, id, visited)
                if res:
                    return True
        return False

    def hasPathCore(self, matrix, row, col, path, id, visited):
        if id == len(path):
            return True

        # if self.visited[row][col] or matrix[row][col] != path[self.id]:
        #     return False

        flag = False
        # an character is found
        if row >= 0 and row < len(matrix) and col >= 0 and col < len(matrix[0]) \
                and not visited[row][col] and matrix[row][col] == path[id]:
            visited[row][col] = 1
            id += 1

            flag = self.hasPathCore(matrix, row, col+1, path, id, visited) \
                    or self.hasPathCore(matrix, row, col-1, path, id, visited) \
                    or self.hasPathCore(matrix, row-1, col, path, id, visited) \
                    or self.hasPathCore(matrix, row+1, col, path, id, visited)
            if not flag:
                id -= 1
                visited[row][col] = 0
        return flag


if __name__ == '__main__':
    so = Solution()
    matrix = [['a','b','c','e'], ['s','f','c','s'], ['a','d','e','e']]
    a = so.hasPath(matrix, 3, 4, 'abs')
    print(a)
