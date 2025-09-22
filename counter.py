#!/usr/bin/env python3
# coding: utf-8

import random
import os
import time

def multiplication(ceil_num_1, ceil_num_2):
    Round = lambda x, n: float(eval('"%.' + str(int(n)) + 'f" % ' + repr(x)))
    while True:
        num_1 = random.randint(0, ceil_num_1)
        num_2 = random.randint(0, ceil_num_2)
        while True:
            print(num_1)
            print('*')
            print(num_2)
            answer = input()
            if  answer == '':
                print('Have a nice day!')
                time.sleep(1)
                os.system('clear')
                exit()
            answer = float(answer)
            if num_1 * num_2 == answer:
                print('ok\n')
                break
            else:
                print('Wrong')

def diff(ceil_num_1, ceil_num_2):
    Round = lambda x, n: float(eval('"%.' + str(int(n)) + 'f" % ' + repr(x)))
    while True:
        while True:
            num_1 = random.randint(0, ceil_num_1)
            num_2 = random.randint(0, ceil_num_2)
            if num_1 >= num_2:
                break
        while True:
            print(num_1)
            print('-')
            print(num_2)
            answer = input()
            if  answer == '':
                print('Have a nice day!')
                time.sleep(1)
                os.system('clear')
                exit()
            answer = float(answer)
            if num_1 - num_2 == answer:
                print('ok\n')
                break
            else:
                print('Wrong')

def difficult_sums():
    Round = lambda x, n: float(eval('"%.' + str(int(n)) + 'f" % ' + repr(x)))
    while True:
        difficulties = [5, 7, 8]
        flor = 0
        ceil = len(difficulties) - 1 
        index_1 = random.randint(flor, ceil)
        index_2 = random.randint(flor, ceil)
        num_1 = difficulties[index_1]
        num_2 = difficulties[index_2]
        while True:
            print(num_1)
            print('+')
            print(num_2)
            answer = input()
            if  answer == '':
                print('Have a nice day!')
                time.sleep(1)
                os.system('clear')
                exit()
            answer = float(answer)
            if num_1 + num_2 == answer:
                print('ok\n')
                break
            else:
                print('Wrong')

def sum_training(ceil_num_1, ceil_num_2):
    Round = lambda x, n: float(eval('"%.' + str(int(n)) + 'f" % ' + repr(x)))
    while True:
        num_1 = random.randint(0, ceil_num_1)
        num_2 = random.randint(0, ceil_num_2)
        while True:
            print(num_1)
            print('+')
            print(num_2)
            answer = input()
            if  answer == '':
                print('Have a nice day!')
                time.sleep(1)
                os.system('clear')
                exit()
            answer = float(answer)
            if num_1 + num_2 == answer:
                print('ok\n')
                break
            else:
                print('Wrong')

def case(banknote):
    Round = lambda x, n: float(eval('"%.' + str(int(n)) + 'f" % ' + repr(x)))
    while True:
        price = random.uniform(0, banknote)
        price = Round(price, 2)
        while True:
            print(banknote)
            print(price)
            answer = input()
            if  answer == '':
                print('Have a nice day!')
                time.sleep(1)
                os.system('clear')
                exit()
            answer = float(answer)
            if price + answer == banknote:
                print('ok\n')
                break
            else:
                print('Wrong')

def change_trainig():
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

    x = random.randint(0, 9)
    if x == 0:
        case(5000)
    if x == 1:
        case(2000)
    if x == 2:
        case(1000)
    if x == 3:
        case(500)
    if x == 4:
        case(200)
    if x == 5:
        case(100)
    if x == 6:
        case(50)
    if x == 7:
        case(10)
    if x == 8:
        case(5)
    if x == 9:
        case(2)

def main():
    print('Select choice: 1 - change, 2 - sum, 3 - sum difficulties, 4 - diff\
            5 - mul')
    choice = input()
    os.system('clear')
    try:
        if int(choice) == 1:
            change_trainig()
        elif int(choice) == 2:
            sum_training(100, 100) # TODO: option for choice
        elif int(choice) == 3:
            difficult_sums()
        elif int(choice) == 4:
            diff(100, 100) # TODO: option for choice
        elif int(choice) == 5:
            multiplication(10, 100) # TODO: option for choice
        else:
            print("Invalid choise. Exiting.")
            exit()
    except ValueError:
        print("Invalid input type. Exiting.")

if __name__ == '__main__':
    main()
