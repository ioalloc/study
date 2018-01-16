#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'xiwei'


class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        for lineno, line in enumerate(board):
            if lineno == 0:

        return board

cases = [
    [
        ['X', 'X', 'X', 'X'],
        ['X', 'O', 'O', 'X'],
        ['X', 'X', 'O', 'X'],
        ['X', 'O', 'X', 'X']
    ],
]

if __name__ == '__main__':
    for case in cases:
        for line in Solution().solve(case):
            print line
