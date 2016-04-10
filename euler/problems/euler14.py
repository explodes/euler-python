#!/usr/bin/env python
from euler.problems.registry import register

LIMIT = 1000000


class MemoizedCollatzSequence:
    MEM = {}

    @staticmethod
    def length_starting_at(n):

        # when n == 1, the sequence is of length 1
        if n == 1:
            return 1

        # if we have memoized the value, return the value
        if n in MemoizedCollatzSequence.MEM:
            return MemoizedCollatzSequence.MEM[n]

        # return the length the current sequence [n] plus the length of rest of the sequence
        n2 = n / 2 if n % 2 == 0 else n * 3 + 1

        length = 1 + MemoizedCollatzSequence.length_starting_at(n2)

        # memoize here for huge performance gains (vs. memoizing the function) (2x faster)
        MemoizedCollatzSequence.MEM[n] = length

        return length


def longest_sequence(n):
    longest_n = 0
    longest_length = 0
    for i in xrange(1, n):
        L = MemoizedCollatzSequence.length_starting_at(i)
        if L > longest_length:
            longest_length = L
            longest_n = i
    return longest_n


@register
class Euler:
    """
    The following iterative sequence is defined for the set of positive integers:

    n -> n/2 (n is even)
    n -> 3n + 1 (n is odd)

    Using the rule above and starting with 13, we generate the following sequence:

    13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
    It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. 
    Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

    Which starting number, under one million, produces the longest chain?

    NOTE: Once the chain starts the terms are allowed to go above one million.
    """
    NUMBER = 14
    NAME = "Longest Collatz sequence"

    def run(self):
        return longest_sequence(LIMIT)

    def test(self):
        assert MemoizedCollatzSequence.length_starting_at(13) == len([13, 40, 20, 10, 5, 16, 8, 4, 2, 1])


if __name__ == '__main__':
    euler = Euler()
    euler.test()
    euler.run()
