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


class AllSubsets(Backtrack):
    """
    Find all subsets in a given list of items.
    Reports 2^n solutions
    """

    def find_all_subsets(self, items):
        N = len(items)
        a = [None] * N
        k = 0
        self.backtrack(a, k, items)

    def is_a_solution(self, a, k, context):
        return k == len(context)

    def construct_candidates(self, a, k, context):
        return [True, False]

    def format_solution(self, a, k, context):
        return [z[1] for z in zip(a, context) if z[0]]


if __name__ == "__main__":
    class SubsetsSaved(AllSubsets, SolutionSaverMixin):
        def all_subsets(self, items):
            self.reset()
            self.find_all_subsets(items)
            return self.solutions


    assert SubsetsSaved().all_subsets([1, 2, 3]) == [[1, 2, 3], [1, 2], [1, 3], [1], [2, 3], [2], [3], []]
