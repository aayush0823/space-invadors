#!/usr/bin/python
# -*- coding: utf-8 -*-
ans = 0
y = []
y.append('|-')
for i in range(1, 9):
    y.append('--')
y.append('-|')
d2 = []
d2.append(y)
for i in range(1, 9):
    d2.append([])
d2.append(y)
for i in range(1, 9):
    d2[i].append('| ')
    for j in range(1, 9):
        d2[i].append('  ')
    d2[i].append(' |')

des = []
des.append([0])
des.append([])
des.append([])
for i in range(1, 3):
    for j in range(0, 9):
        des[i].append(0)

mark = []
for i in range(0, 9):
    x = []
    for j in range(0, 9):
        x.append(0)
    mark.append(x)
