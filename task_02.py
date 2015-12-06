#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Wk14 - Synthetizing tasks Task 2 """

import task_01


def fibo(count):
    """
    Creates a list of the Fibonacci sequence
    Args:
        count (int): Count of numbers in the sequence
    Returns:
        list: Fibonacci sequence
    Examples:
        >>> fibo(5)
        [0, 1, 1, 2, 3]
    """

    return [x for x in task_01.xfibo(count)]
