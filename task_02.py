#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Custom exception class for additional functionality in debugging errors"""

class CustomError(Exception):
    """Custom exception class"""
    def __init__(self, message, cause):
        Exception.__init__(self, message)
        self.cause = cause
