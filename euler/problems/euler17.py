#!/usr/bin/env python
from euler.problems.registry import register

LIMIT = 1000
DIGITS = {
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
}

PREFIXED = (
    (90, "ninety"),
    (80, "eighty"),
    (70, "seventy"),
    (60, "sixty"),
    (50, "fifty"),
    (40, "forty"),
    (30, "thirty"),
    (20, "twenty"),
)

POSTFIXED = (
    (1000, "thousand"),
    (100, "hundred"),
)


def as_words(n):
    # this very much reminds me of the roman numeral kata..

    if n == 0:
        return ""

    parts = []

    for val, name in POSTFIXED:
        if n >= val:
            d = n / val
            parts.append(as_words(d))
            parts.append(name)
            n -= (d * val)

    for val, name in PREFIXED:
        if n >= val:
            d = n - val
            s = name
            if d > 0:
                s += "-" + as_words(d)
            if parts:
                parts.append("and")
            parts.append(s)
            break
    else:
        if n in DIGITS:
            if parts:
                parts.append("and")
            parts.append(DIGITS[n])

    return " ".join(parts)


def count_letters(n):
    words = as_words(n)
    return len(words.replace("-", "").replace(" ", ""))


def count_letters_of_range(n):
    return sum(count_letters(i) for i in xrange(1, n + 1))


@register
class Euler:
    """
    If the numbers 1 to 5 are written out in words: one, two, three, four, five,
    then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

    If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be
    used?

    NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters
    and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in
    compliance with British usage.
    """
    NUMBER = 17
    NAME = "Number letter counts"
    ANSWER = 21124

    def run(self):
        return count_letters_of_range(LIMIT)

    def test(self):
        def check(val, name):
            words = as_words(val)
            print val, "->", words
            assert words == name

        check(1, "one")
        check(9, "nine")
        check(10, "ten")
        check(11, "eleven")
        check(20, "twenty")
        check(25, "twenty-five")
        check(99, "ninety-nine")
        check(100, "one hundred")
        check(101, "one hundred and one")
        check(115, "one hundred and fifteen")
        check(563, "five hundred and sixty-three")
        check(1000, "one thousand")
        check(2798, "two thousand seven hundred and ninety-eight")

        assert count_letters_of_range(5) == 19


if __name__ == '__main__':
    euler = Euler()
    euler.test()
    euler.run()
