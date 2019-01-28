#!/usr/bin/python
# -*- coding: utf-8 -*-


class Alien:

    def __init__(self, x, y):
        self.x = x
        self.y = y


class spaceship:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def left(self):
        if self.y != 1:
            self.y = self.y - 1

    def right(self):
        if self.y != 8:
            self.y = self.y + 1


class miss:

    def __init__(self, x, y):
        self.x = x
        self.y = y


class miss1(miss):

    def __init__(self, x, y):
        miss.__init__(self, x, y)

    def move(self):
        self.x = self.x + 1


class miss2(miss):

    def __init__(self, x, y):
        miss.__init__(self, x, y)

    def move(self):
        self.x = self.x + 2
