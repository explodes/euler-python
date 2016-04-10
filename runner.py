#!/usr/bin/env python
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
    for klass in _matching_problems(items, number):
        print 'test #%d: %s' % (klass.NUMBER, klass.NAME)
        klass.test()


def run_problems(items, number):
    for klass in _matching_problems(items, number):
        now = time()
        header = 'Euler #%d: %s' % (klass.NUMBER, klass.NAME)

        print header.ljust(64), str(klass.run()).rjust(32),
        then = time()
        print "%.4fs" % (then - now)


def main(number, test):
    from euler.problems import registry
    if test:
        run_tests(registry.REGISTRY, number)
    else:
        run_problems(registry.REGISTRY, number)


if __name__ == '__main__':
    (options, args) = parser.parse_args()
    main(options.number, options.test)
