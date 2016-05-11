#!/usr/bin/env python
# coding=utf-8
"""
Support for the backtrack combinatorial algorithm provided in

The Algorithm Design Manual 2nd Edition - Steven S. Skiena
Copyright 2010 Springer-Verlag London Limited
ISB: 978-1-84996-720-4

Backtrack-DFS(A, k)
    if A = (a1, a2, ..., ak) is a solution, report it
    else
        k = k + 1
        compute Sk
        while Sk != ∅
            ak = an element in Sk
            Sk = Sk - ak
            Backtrack-DFS(A, k)
"""


class Backtrack(object):
    """
    Backtrack Algorithm as per Skiena p232

    Subclasses must implement `report_solution(a, k, context)`
    """

    def __init__(self):
        self.finished = False

    def backtrack(self, a, k, context=None):
        self.finished = False
        self.backtrack_helper(a, k, context)

    def backtrack_helper(self, a, k, context):
        """
        Meat of the backtrack algorithm
        :param a: solution candidate
        :param k: current index of the potential solution being evaluated
        :param context: contextual information
        """
        if self.is_a_solution(a, k, context):
            solution = self.format_solution(a, k, context)
            self.report_solution(solution)
        else:
            candidates = self.construct_candidates(a, k, context)
            if candidates:
                for candidate in candidates:
                    a[k] = candidate
                    self.make_move(a, k, candidate, context)
                    self.backtrack_helper(a, k + 1, context)
                    self.unmake_move(a, k, candidate, context)
                    if self.finished:
                        return  # terminate early

    def is_a_solution(self, a, k, context):
        """
        Consider a possible solution `a` as a valid solution
        :param a: solution candidate
        :param k: current index of the potential solution being evaluated
        :param context: contextual information
        :return True or False
        """
        return True

    def format_solution(self, a, k, context):
        """
        Format a solution before reporting it
        :param a: solution candidate
        :param k: current index of the potential solution being evaluated
        :param context: contextual information
        :return: formatted solution
        """
        return a

    def construct_candidates(self, a, k, context):
        """
        Create candiates for the next move at position `k`
        :param a: solution candidate
        :param k: current index of the potential solution being evaluated
        :param context: contextual information
        :return: array of candidates at position `k`
        """
        return None

    def make_move(self, a, k, candidate, context):
        """
        Optimization hint to perform a single move
        :param a: solution candidate
        :param k: current index of the potential solution being evaluated
        :param candidate: candidate under consideration
        :param context: contextual information
        """
        pass

    def unmake_move(self, a, k, candidate, context):
        """
        Optimization hint to undo a single move
        :param a: solution candidate
        :param k: current index of the potential solution being evaluated
        :param candidate: candidate under consideration
        :param context: contextual information
        """
        pass


class SolutionHandler(object):
    def report_solution(self, solution):
        """
        Handle the reporting of a solution
        :param solution formatted solution
        """
        pass


class SolutionPrinterMixin(SolutionHandler):
    def report_solution(self, solution):
        print solution


class SolutionSaverMixin(SolutionHandler):
    solutions = []

    def reset(self):
        self.solutions = []

    def report_solution(self, solution):
        self.solutions.append(solution)


class Subsets(Backtrack):
    """
    Find all subsets in a given list of items.
    Reports 2^n solutions
    """

    def find_subsets(self, items):
        a = [None] * len(items)
        self.backtrack(a, 0, items)

    def is_a_solution(self, a, k, items):
        return k == len(items)

    def construct_candidates(self, a, k, items):
        return [True, False]

    def format_solution(self, a, k, items):
        return [z[1] for z in zip(a, items) if z[0]]


class Permutations(Backtrack):
    """
    Permutation Backtrack algorithm as per Skiena p235
    """
    SENTINEL = object()  # guaranteed unique item to which nothing else may be equal

    def find_permutations(self, items):
        a = [Permutations.SENTINEL] * len(items)
        self.backtrack(a, 0, items)

    def construct_candidates(self, a, k, items):
        return [c for c in items if not c in a[:k]]

    def is_a_solution(self, a, k, items):
        return k == len(items)


if __name__ == "__main__":
    class SubsetsSaved(Subsets, SolutionSaverMixin):
        def subsets(self, items):
            self.reset()
            self.find_subsets(items)
            return self.solutions


    class PermutationsSaved(Permutations, SolutionSaverMixin):
        def format_solution(self, a, k, context):
            return a[:]

        def permutations(self, items):
            self.reset()
            self.find_permutations(items)
            return self.solutions


    assert SubsetsSaved().subsets([1, 2, 3]) == \
           [[1, 2, 3], [1, 2], [1, 3], [1], [2, 3], [2], [3], []]

    assert PermutationsSaved().permutations([1, 2, 3]) == \
           [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
