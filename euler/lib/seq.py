#!/usr/bin/env python


def bin_index(L, item, low=0, high=None):
    """
    Perform a binary search on ordered sequence L
    O(lg n)
    :param L: ordered sequence to scan
    :param item: `item` to search for
    :param low: lowest bound to search in `L`
    :param high: highest bound to search in `L`
    :return: The proposed index of `item`.
    """
    if high is None:
        high = len(L)

    index = low + (high - low) / 2

    if L[index] == item:
        return index
    elif index == low:
        # proposed location
        if item < L[index]:
            # < N, proposed index = N
            return index
        else:
            # > N, proposed index = N + 1
            return index + 1

    if item < L[index]:
        return bin_index(L, item, low, index)
    else:
        return bin_index(L, item, index, high)


def bin_search(L, item):
    """
    Perform a binary search for `item` in sorted sequence `L`
    O(lg n)
    :param L: sorted sequence
    :param item: item to search for
    :return: -1, or the found index
    """
    index = bin_index(L, item)
    N = len(L)
    if index >= N or L[index] != item:
        return -1
    return index


def insert_in_order(L, item):
    """
    Insert i into `L` in order with or without duplicates
    O(lg n)
    :param L: list to add to
    :param item: item to insert
    """
    index = bin_index(L, item)
    L.insert(index, item)


if __name__ == '__main__':

    # Tests

    # bin index
    seq = [0, 10, 20, 35, 400, 2002, 3003, 5000, 10000]
    assert bin_index(seq, -1) == 0
    assert bin_index(seq, 0) == 0
    assert bin_index(seq, 20) == 2
    assert bin_index(seq, 21) == 3
    assert bin_index(seq, 36) == 4
    assert bin_index(seq, 10000) == 8
    assert bin_index(seq, 100001) == 9

    # bin insert
    seq = [10, 20, 30]
    insert_in_order(seq, 11)
    assert seq == [10, 11, 20, 30]
    insert_in_order(seq, 9)
    assert seq == [9, 10, 11, 20, 30]
    insert_in_order(seq, 30)
    assert seq == [9, 10, 11, 20, 30, 30]
    insert_in_order(seq, 31)
    assert seq == [9, 10, 11, 20, 30, 30, 31]

    # bin search
    seq = [0, 1, 2, 3, 4]
    for x in seq:
        i = bin_search(seq, x)
        assert i == x, '%d found at incorrect index %d' % (x, i)
    assert bin_search(seq, -1) == -1
    assert bin_search(seq, 5) == -1
