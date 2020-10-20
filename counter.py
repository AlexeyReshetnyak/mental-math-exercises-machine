#!/usr/bin/env python3
# coding: utf-8

import random

#def case():

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

    Round = lambda x, n: float(eval('"%.' + str(int(n)) + 'f" % ' + repr(x)))
    x = random.randint(0, 10)
    x = 0
    if x == 0:
        while True:
            banknote = random.uniform(0, 5000)
            banknote = Round(banknote, 2)
            while True:
                print(5000)
                print(banknote)
                answer = float(input())
                if banknote + answer == 5000:
                    print('ok\n')
                    break
                else:
                    print('Wrong')
        
    if x == 1:
        print(x)

if __name__ == '__main__':
    main()

