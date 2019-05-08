#!/usr/bin/env python

# encoding: utf-8

'''

@author: Jason Lee

@license: (C) Copyright @ Jason Lee

@contact: jiansenll@163.com

@file: jianzhi_offer_40_1.py

@time: 2019/5/8 15:33

@desc:

'''


# 从头到尾依次异或数组中的每一个数字，那么最终得到的结果就是两个只出现一次的数字的异或结果。因为其它数字都出现了两次，在异或中全部抵消掉了。
class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        if len(array) <= 2:
            return array
        # 对所有数据求异或
        temp = array[0]
        for i in array[1:]:
            temp ^= i
        # 由于这两个数字肯定不一样，那么这个异或结果肯定不为0 ，也就是说在这个结果数字的二进制表示中至少就有一位为1 。
        # 我们在结果数字中找到第一个为1 的位的位置，记为第N位。
        idx = 0
        while temp & 1 == 0:
            temp = temp >> 1
            idx += 1
        # 现在我们以第N 位是不是1 为标准把原数组中的数字分成两个子数组，
        # 第一个子数组中每个数字的第N 位都为1 ，而第二个子数组的每个数字的第N 位都为0 。
        # 这样可以保证把两个单独只出现一次的数，分配到两个子数组中去。
        a = 0  # 0与一个数的异或，仍是那个数
        b = 0
        for i in array:
            if self.isBit(i, idx):
                a ^= i
            else:
                b ^= i
        return [a, b]

    # 判断data的第idx位是否是1
    def isBit(self, data, idx):
        temp = data >> idx
        return temp & 1


if __name__ == '__main__':
    array = [1, 2, 2, 3]
    res = Solution()
    a = res.FindNumsAppearOnce(array)
    print(a)
