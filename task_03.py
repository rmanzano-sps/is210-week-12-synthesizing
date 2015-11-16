#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 03 module"""

def exception_test(arg1, arg2, arg3):
    """Takes in three arguments and returns errors captured"""
    caught = False
    try:
        arg1[arg2].index(arg3)
    except(TypeError, LookupError):
        caught = True

    return caught
