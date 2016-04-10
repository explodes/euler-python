#!/usr/bin/env python
# coding=utf-8
import sys
from time import time
from optparse import OptionParser

parser = OptionParser()
parser.add_option("-n", "--number", dest="number", type="int",
                  help="problem to run or test", metavar="NUMBER")
parser.add_option("-t", "--test",
                  action="store_true", dest="test", default=False,
                  help="run tests")


def _matching_problems(items, number):
    for klass in items:
        if number is None or klass.NUMBER == number:
            yield klass()


def run_tests(items, number):
    for problem in _matching_problems(items, number):
        print 'test #%d: %s' % (problem.NUMBER, problem.NAME)
        problem.test()


def run_problems(items, number):
    print "problem".ljust(50), "result".rjust(24), "   ", "answer".ljust(24), "time".rjust(7)
    print "=" * (50 + 24 + 3 + 24 + 6 + 5)

    for problem in _matching_problems(items, number):
        header = 'Euler #%d: %s' % (problem.NUMBER, problem.NAME)

        answer = getattr(problem, 'ANSWER', 'unknown')

        then = time()
        result = problem.run()
        now = time()

        equals = "[?]" if answer == "unknown" else ("[✓]" if answer == result else "[✗]")

        print header.ljust(50), str(problem.run()).rjust(24), equals, str(answer).ljust(24), "%.4fs" % (now - then)


def main(number, test):
    from euler.problems import registry
    if test:
        run_tests(registry.REGISTRY, number)
    else:
        run_problems(registry.REGISTRY, number)


if __name__ == '__main__':
    (options, args) = parser.parse_args()
    main(options.number, options.test)
