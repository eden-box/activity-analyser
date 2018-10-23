#!/usr/bin/env python3.7

from .log_filter_exception import LogFilterException


class FullDefaultException(LogFilterException):
    """
    Exception raised when an entry is added to a Default Priority queue
    """
    pass
