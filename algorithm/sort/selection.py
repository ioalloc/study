#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'xiwei'


def sort(seq):
    """

    :param seq:
    :type seq: list
    :return:
    """
    for i in xrange(0, len(seq)):
        mi = i
        for j in xrange(i+1, len(seq)):
            if seq[j] < seq[mi]:
                mi = j
        seq[i], seq[mi] = seq[mi], seq[i]
    return seq


print sort([1, 4, 5, 3, 2])
