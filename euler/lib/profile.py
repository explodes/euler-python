# coding=utf-8
from functools import wraps
from time import time as t


def log(callable, *args, **kwargs):
    name = callable.__name__

    if args and kwargs:
        print '--> %s(%s, %s)' % (name, args, kwargs)
    elif args:
        print '--> %s(%s)' % (name, args)
    elif kwargs:
        print '--> %s(%s)' % (name, kwargs)
    else:
        print '--> %s()' % name

    result = callable(*args, **kwargs)
    print '<-- %s => %s' % (name, result)
    return result


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
