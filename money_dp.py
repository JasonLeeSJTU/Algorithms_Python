#!/usr/bin/env python

# encoding: utf-8

'''

@author: Jason Lee

@license: (C) Copyright @ Jason Lee

@contact: jiansenll@163.com

@file: money_dp.py

@time: 2019/4/22 23:17

@desc:
find least number of money to achieve a total amount
'''

def money_dp(total):
    money = [1, 5, 11]  # value of each money
    number = [0]*(total+1)    # we need number[i] changes to achieve totally i money

    for i in range(1, total + 1):
        cost = float('inf')
        if i - money[2] >= 0:
            cost = min(cost, number[i - money[2]] + 1)
        if i - money[1] >= 0:
            cost = min(cost, number[i - money[1]] + 1)
        if i - money[0] >= 0:
            cost = min(cost, number[i - money[0]] + 1)

        number[i] = cost
        print(f"f[{i}] = {number[i]}")

    return number[total]


def money_dp_output(total):
    money = [1, 5, 11]
    number = [0]*(total+1)
    vector = [0]*(total+1)
    for i in range(1, total+1):
        cost = float('inf')
        value = 0
        for j in money:
            if i-j >= 0 and cost > number[i-j] + 1:
                cost = number[i-j] + 1
                value = j
        number[i] = cost
        vector[i] = value


        print(f"f[{i}] = {number[i]}")

    return number[total], vector

if __name__ == '__main__':
    total = 5
    _, vector = money_dp_output(total)
    combine = []
    k = total
    while k>0:
        combine.append(vector[k])
        k = k - vector[k]

    print(combine)