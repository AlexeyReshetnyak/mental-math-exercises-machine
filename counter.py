#!/usr/bin/env python3
# coding: utf-8

import random

def case(banknote):
    Round = lambda x, n: float(eval('"%.' + str(int(n)) + 'f" % ' + repr(x)))
    while True:
        price = random.uniform(0, banknote)
        price = Round(price, 2)
        while True:
            print(banknote)
            print(price)
            answer = float(input())
            if price + answer == banknote:
                print('ok\n')
                break
            else:
                print('Wrong')

def main():
    # 0 - 5000
    # 1 - 2000
    # 3 - 1000
    # 4 - 500
    # 5 - 200
    # 6 - 100
    # 7 - 50
    # 8 - 10
    # 9 - 5
    # 10 -2

    x = random.randint(0, 10)
    x = 1 #TODO: remove
    if x == 0:
        case(5000)
    if x == 1:
        case(2000)

if __name__ == '__main__':
    main()
