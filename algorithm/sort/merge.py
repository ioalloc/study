#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'xiwei'


def sort(seq):
    """

    :param seq:
    :return:
    """
    size = len(seq)
    if size < 2:
        return seq
    else:
        return merge(sort(seq[0:size/2]), sort(seq[size/2:]))


def merge(left, right):
    """
    :param left:
    :param right:
    :type right: list
    :return:
    """
    result = []
    for l in left:
        while len(right) > 0 and l > right[0]:
            result.append(right.pop(0))
        result.append(l)
    result += right
    return result


print sort([1, 9, 3, 2])
