#!/usr/bin/env python
# coding=utf-8
import sys
from optparse import OptionParser
from time import time

parser = OptionParser()
parser.add_option("-n", "--number", dest="number", type="int",
                  help="problem to run or test", metavar="NUMBER")
parser.add_option("-t", "--test",
                  action="store_true", dest="test", default=False,
                  help="run tests")
parser.add_option("-u", "--unsolved",
                  action="store_true", dest="unsolved", default=False,
                  help="only show unsolved problems")


def _matching_problems(number, unsolved):
    from euler.problems import registry
    for klass in registry.REGISTRY:
        if unsolved:
            if klass.ANSWER is None:
                yield klass()
        elif number is None or klass.NUMBER == number:
            yield klass()


def run_tests(problems):
    for problem in problems:
        print 'test #%d: %s' % (problem.NUMBER, problem.NAME)
        problem.test()


def run_problems(problems):
    print "problem".ljust(50), "answer".rjust(24), "   ", "result".ljust(24), "time".rjust(7)
    print "=" * (50 + 24 + 3 + 24 + 6 + 5)

    for problem in problems:
        header = 'Euler #%d: %s' % (problem.NUMBER, problem.NAME)

        answer = getattr(problem, 'ANSWER', 'unknown')
        if answer in [None, "unknown"]:
            answer = "unknown"

        print header.ljust(50), str(answer).rjust(24),
        sys.stdout.flush()

        then = time()
        result = problem.run()
        now = time()

        equals = "[?]" if answer == "unknown" else ("[✓]" if answer == result else "[✗]")

        print equals, str(result).ljust(24), "%.4fs" % (now - then)


def main(number, test, unsolved):
    if test:
        problems = _matching_problems(number, unsolved)
        run_tests(problems)
    else:
        problems = _matching_problems(number, unsolved)
        run_problems(problems)


if __name__ == '__main__':
    (options, args) = parser.parse_args()
    main(options.number, options.test, options.unsolved)
