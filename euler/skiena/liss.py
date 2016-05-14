#!/usr/bin/env python
# coding=utf-8
"""
Longest increasing subsequence
"""
from euler.lib.seq import bin_index
from euler.lib.profile import time


@time
def longest_increasing_subsequence_r(s):
    return longest_increasing_subsequence_r_helper(s, [], 0)


def longest_increasing_subsequence_r_helper(s, a, k):
    if k == len(s):
        return a

    max_seq = a
    N = len(a)
    max_len = N

    for i in xrange(k, len(s)):
        next_item = s[i]
        b = a[:]
        if N == 0 or next_item >= b[-1]:
            b.append(next_item)
            next_seq = longest_increasing_subsequence_r_helper(s, b, i + 1)
            next_len = len(next_seq)
            if next_len > max_len:
                max_seq, max_len = next_seq, next_len

    return max_seq


def walk_parent(seq, parents, start):
    # walk backward through the parent graph
    s = []
    while start != -1:
        j = seq[start]
        s.append(j)
        start = parents[start]

    return s[::-1]


def longest_increasing_subsequence_dp(s):
    N = len(s)

    lengths = [None] * N  # storage for the longest run for each item
    parents = [-1] * N  # parent element for longest subsequence

    # our best solution initially is [s[0]]
    max_len = 1
    best_end = 0
    lengths[0] = 1
    parents[0] = -1

    for i in xrange(1, N):
        lengths[i] = 1
        parents[i] = -1
        for j in xrange(i - 1, 0 - 1, -1):
            if lengths[j] >= lengths[i] and s[j] < s[i]:
                lengths[i] = lengths[j] + 1
                parents[i] = j
        if lengths[i] > max_len:
            best_end = i
            max_len = lengths[i]

    return walk_parent(s, parents, best_end)


def first_gte(seq, c, indices=None):
    if indices is None:
        indices = range(len(seq))

    start = 0
    end = len(indices) - 1

    while start != end:
        i = start + (end - start) / 2
        if seq[indices[i]] < c:
            start = i + 1
        else:
            end = i

    return start


def longest_increasing_subsequence_nlogn(seq):
    N = len(seq)
    indices = [0]
    parents = [-1] * N

    for index in xrange(1, N):
        item = seq[index]
        if item > seq[indices[-1]]:
            parents[index] = indices[-1]
            indices.append(index)
        else:
            i = first_gte(seq, item, indices)
            indices[i] = index
            parents[index] = indices[i - 1]

    return walk_parent(seq, parents, indices[-1])


if __name__ == '__main__':
    def test_algorithms(seq, target):

        for limit, algo in (
                (10 ** 12, longest_increasing_subsequence_nlogn),
                (10 ** 3, longest_increasing_subsequence_dp),
                (19, longest_increasing_subsequence_r)
        ):
            if len(seq) > limit:
                print algo.__name__, 'too slow for', len(seq), 'elements'
                continue
            f = time(algo)
            liss = f(seq)
            assert len(liss) == target
            m = liss[0]
            for c in liss[1:]:
                assert c > m, "not ascending order"
                m = c


    assert walk_parent(range(100), (-1, 0, 1, 2, 3), 4) == [0, 1, 2, 3, 4]

    assert walk_parent(range(100), (-1, 0, 1, 2, 1), 4) == [0, 1, 4]

    assert first_gte((0, 1, 2), 0) == 0
    assert first_gte((0, 1, 2), 1) == 1
    assert first_gte((0, 1, 2), 2) == 2
    assert first_gte((2, 4), 3) == 1
    assert first_gte((2, 4, 4, 4, 4), 3) == 1

    assert longest_increasing_subsequence_nlogn((2, 6, 3, 4, 1, 2, 9, 5, 8)) == [2, 3, 4, 5, 8]

    test_algorithms((2, 4, 3, 5, 1, 7, 6, 9, 8), 5)
    test_algorithms((2, 4, 3, 5, 1, 7, 6, 9, 8, 10, 11, 12, 13, 14, 15, 16, 17), 13)
    test_algorithms(range(20), 20)
    test_algorithms(range(40), 40)
    test_algorithms(range(1000), 1000)
