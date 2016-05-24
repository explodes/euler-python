def is_palindrome(seq):
    """
    Determine if a sequence is a palindrome
    """
    # after benchmarks, this is faster than comparing characters
    # from either end converging toward the center.
    # it is also faster than comparing two substrings, one reversed, each of length N /2
    return seq == seq[::-1]
