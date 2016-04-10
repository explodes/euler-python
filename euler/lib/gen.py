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
    item = next(gen)
    try:
        while True:
            item = next(gen)
    except StopIteration:
        pass
    return item


def gen_len(gen):
    i = 0
    try:
        while True:
            next(gen)
            i += 1
    except StopIteration:
        pass
    return i
