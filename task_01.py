#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Wk14 - Synthetizing tasks Task 01"""


def xfibo(count):
    """Fibo sequence generator
 
    Args:
        count (int): Number of integers to return in the sequence.

    Returns:
        list: A number in the Fibonacci sequence.

    Examples:
        >>> [x for x in xfibo(10)]
        [0, 1, 1, 2, 3, 5, 8]
    """
    iteration = 0
    lastnum, curnum = 0, 1
    numbers = [lastnum]
    yield lastnum
    while iteration < count - 1:
        yield curnum
        lastnum, curnum = curnum, lastnum + curnum
        iteration += 1

