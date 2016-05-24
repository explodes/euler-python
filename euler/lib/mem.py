from functools import wraps


def function_args(*args, **kwargs):
    return args


def memoize(known=None, memoize_on=function_args):
    """
    Wrap a function for memoization, optionally providing a dictionary of values that are already known.
    Wrapped functions cannot accept kwargs.
    """
    known = {} if known is None else {}

    def decorator(func):
        func.__memoized = known

        @wraps(func)
        def wrapped(*args, **kwargs):
            if kwargs:
                raise Exception("Kwargs not supported in memoization")
            key = memoize_on(*args, **kwargs)
            if key in known:
                return known[key]
            result = func(*args, **kwargs)
            known[key] = result
            return result

        return wrapped

    return decorator
