from functools import wraps


def memoize(known=None):
    """
    Wrap a function for memoization, optionally providing a dictionary of values that are already known.
    Wrapped functions cannot accept kwargs.
    """
    known = {} if known is None else {}

    def decorator(func):
        @wraps(func)
        def wrapped(*args, **kwargs):
            if kwargs:
                raise Exception("Kwargs not supported in memoization")
            if args in known:
                return known[args]
            result = func(*args)
            known[args] = result
            return result

        return wrapped

    return decorator
