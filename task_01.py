#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Creating custom exception classes"""

class BaseError(Exception):
    """Exception Class"""
    pass

class StringError(BaseError, TypeError):
    """Subclassed to BaseError and TypeError"""
    pass

class NumberError(BaseError, TypeError):
    """Subclassed to BaseError and TypeError"""
    pass

class NonZeroError(NumberError):
    """Subclassed to NumberError"""
    pass
