#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'xiwei'

from downer import Downer
import time


class Upper:
    def __init__(self):
        self.pos = 0

    def forwards(self):
        self.pos += 1

    def back(self):
        self.pos -= 1

    def render(self):
        print self.pos

    def run(self):
        for x in xrange(0, 20):
            Downer().run()
            time.sleep(1)
        

if __name__ == '__main__':
    Upper().run()

