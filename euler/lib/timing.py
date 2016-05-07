# coding=utf-8
from functools import wraps
from time import time as t


def time(func):
    """
    Time a function.
    Log the time, parameters, and result of a function.
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        sig = "%s(%s, %s)" % (func.__name__, args, kwargs)
        print "→ %s" % sig
        then = t()
        result = func(*args, **kwargs)
        now = t()
        print "← %s :: %0.6fs ⇒ %s" % (sig, (now - then), result)
        return result

    return wrapper
