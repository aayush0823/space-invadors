#!/usr/bin/python
# -*- coding: utf-8 -*-
from modules import *
from glob import *


def Print():
    os.system('clear')
    for i in range(0, 10):
        xx = ''
        for j in range(0, 10):
            xx = xx + d2[i][j]
        print (xx)
    print ('Points')
    print (ans)


def isData():
    return select.select([sys.stdin], [], [], 0) == ([sys.stdin], [],
            [])


def alien(time):
    x = random.randint(1, 2)
    y = random.randint(1, 8)
    des[x][y] = time
    os.system('clear')
    d2[x][y] = '@ '
    Print()


def missile():
    global ans
    global des
    global mark
    for i in range(1, 9):
        for j in range(1, 9):
            if d2[i][j] == 'i ' or mark[i][j] == 1:
                d2[i][j] = '  '
                if d2[i - 1][j] == '@ ' or d2[i - 1][j] == 'a ':
                    ans += 1
                    d2[i - 1][j] = '  '
                elif i != 1:
                    d2[i - 1][j] = 'i '
            if d2[i][j] == 'l ' or mark[i][j] == 1:
                d2[i][j] = '  '
                if d2[i - 1][j] == '@ ' or d2[i - 1][j] == 'a ':
                    d2[i - 1][j] = 'a '
                    des[i - 1][j] += 5
                elif d2[i - 2][j] == '@ ' or d2[i - 1][j] == 'a ':
                    d2[i - 2][j] = 'a '
                    des[i - 2][j] += 5
                elif i > 2:
                    if d2[i - 2][j] == 'i ':
                        mark[i - 2][j] = 1
                    d2[i - 2][j] = 'l '
                mark[i][j] = 0
    Print()
