#!/usr/bin/env python

# encoding: utf-8

'''

@author: Jason Lee

@license: (C) Copyright @ Jason Lee

@contact: jiansenll@163.com

@file: jianzhi_offer_44.py

@time: 2019/4/26 17:03

@desc:

'''
import random
import copy
class Solution:
    def IsContinuous(self, numbers):
        # define the sequence of 56 cards
        # heart spade club diamond king
        card = []
        num_king = 0
        # get cards
        for i in range(5):
            idx = random.randint(0, 56)
            # assign the card number
            if idx < 13:
                card.append(idx + 1) # card number starts from 1
            elif idx < 26:
                card.append(idx - 13 + 1)
            elif idx < 39:
                card.append(idx - 26 + 1)
            elif idx < 52:
                card.append(idx - 39 + 1)
            else:
                card.append(0)  # king is chosen
                num_king += 1

        # verify
        flag = True
        max_val = max(card)
        for i in range(1, 5):
            if not max_val - i or max_val - i not in card:  # in case max_val - i == 0
                num_king -= 1   # use king card to replace this number
                if num_king < 0:
                   flag = False
                   break

        return flag, card

if __name__ == '__main__':
    res = Solution()
    f, c = res.IsContinuous(1)
    print(f, c)