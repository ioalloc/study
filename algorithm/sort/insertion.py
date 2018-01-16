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

        for j in xrange(i, 1, -1):
            if seq[j] < seq[j-1]:
                seq[j], seq[j-1] = seq[j-1], seq[j]
            else:
                break
    return seq


print sort([1, 4, 6, 2, 5, 1])
