#!/usr/bin/python
# -*- coding: utf-8 -*-

from modules import *
from classes import *

from glob import *

from functions import *

S = spaceship(8, 4)
d2[S.x][S.y] = 'X '
Print()
old_settings = termios.tcgetattr(sys.stdin)
start = time.time()
alien(time.time() - start + 8)
timer = time.time() - start
timer2 = time.time() - start
flag = 1
flagm1 = 0
try:
    tty.setcbreak(sys.stdin.fileno())
    while 1:
        t0 = time.time() - start

        if t0 % 10 < 0.0001 and t0 % 10 > -0.0001 and flag == 0:
            alien(t0 + 8)
            timer = time.time() - start
            flag = 1
        if t0 - timer > 2:
            flag = 0

        if t0 % 1 < 0.0001 and t0 % 1 > -0.0001 and flagm1 == 0:
            missile()
            timer2 = time.time() - start
            flagm1 = 1
        if t0 - timer2 > 0.5:
            flagm1 = 0

        for i in range(1, 3):
            for j in range(1, 9):
                if des[i][j] - t0 < 0.0001 and des[i][j] - t0 > -0.0001:
                    d2[i][j] = '  '
                    des[i][j] = 0
        if isData():
            c = sys.stdin.read(1)
            if c == 'q':
                break
            if c == 'a':
                d2[S.x][S.y] = '  '
                S.left()
                d2[S.x][S.y] = 'X '
                Print()
            if c == 'd':
                d2[S.x][S.y] = '  '
                S.right()
                d2[S.x][S.y] = 'X '
                Print()
            if c == ' ':
                M = miss1(S.x - 1, S.y)
                d2[M.x][M.y] = 'i '
                flagm1 = 1
                Print()
            if c == 's':
                M2 = miss2(S.x - 1, S.y)
                d2[M2.x][M2.y] = 'l '
                Print()
finally:
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_settings)
