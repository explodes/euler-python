#!/usr/bin/env python
# coding=utf-8
from euler.problems.registry import register


@register
class Euler:
    """
    The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1); so the first ten triangle numbers are:

    1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

    By converting each letter in a word to a number corresponding to its alphabetical position and adding these values
    we form a word value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value is a
    triangle number then we shall call the word a triangle word.

    Using p042_words.txt, a 16K text file containing nearly two-thousand common
    English words, how many are triangle words?
    """
    NUMBER = 42
    NAME = "Coded triangle numbers"
    ANSWER = None

    def run(self):
        return "NOT IMPLEMENTED"

    def test(self):
        pass


if __name__ == '__main__':
    euler = Euler()
    euler.test()
    print euler.run()
