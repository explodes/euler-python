def first_n(gen, n):
    """
    Get the first n items from a generator
    """
    count = 0
    results = []
    while count < n:
        results.append(next(gen))
        count += 1
    return results


def item_n(gen, n):
    """
    Get the nth zero-based item from a generator
    """
    count = 0
    result = next(gen)
    while count < n:
        result = next(gen)
        count += 1
    return result


def last_item(gen):
    """
    Get the last item from a generator.
    The generator will be exhausted.
    If the generator is infinite, this will not return.
    """
    item = next(gen)
    try:
        while True:
            item = next(gen)
    except StopIteration:
        pass
    return item


def gen_len(gen):
    """
    Get the length of a generator.
    The generator will be exhausted.
    If the generator is infinite, this will not return.
    """
    i = 0
    try:
        while True:
            next(gen)
            i += 1
    except StopIteration:
        pass
    return i


def lrange(a, b=None, step=None):
    """
    Use in place of xrange when the range can overflow.
    """
    if b is None:
        start = 0
        stop = a
    else:
        start = a
        stop = b

    i = start
    while i < stop:
        yield i
        i += step
