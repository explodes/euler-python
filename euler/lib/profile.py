# coding=utf-8
from functools import wraps
from time import time as current_time


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
        then = current_time()
        result = func(*args, **kwargs)
        now = current_time()
        print "← %s :: %0.6fs ⇒ %s" % (sig, (now - then), result)
        return result

    return wrapper


class Timer(object):
    def __init__(self, message=None):
        self.message = message
        self.start_time = None
        self.end_time = None
        self.iterations = 0
        self.running_total = 0

    def start(self, message=None):
        """
        Start this timer (possibly again) with an optional message
        :param message: optional message (overrides message on init)
        :return: self, for chaining
        """
        if message is not None:
            self.message = message

        self.start_time = current_time()
        return self

    def end(self, message=None):
        """
        End this timer (possibly again) with an optional message
        :param message: optional message (overrides message on init)
        :return: self, for chaining
        """
        if message is not None:
            self.message = message

        self.end_time = current_time()
        self.iterations += 1
        self.running_total += self.duration
        return self

    @property
    def duration(self):
        if self.start_time is None or self.end_time is None:
            return None
        else:
            return self.end_time - self.start_time

    @property
    def average(self):
        if self.iterations > 0:
            return self.running_total / self.iterations
        else:
            return 0

    @staticmethod
    def format_value(f):
        if f is None:
            return "None"
        else:
            return "%0.6fs" % f

    def log(self):
        """
        Log the current results of this timer (last duration, average duration of each iteration)
        """
        average_note = " (avg: %s)" % Timer.format_value(self.average)
        print "%s took %s%s" % (self.message, Timer.format_value(self.duration), average_note)
