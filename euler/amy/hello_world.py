#!/usr/bin/env python


print 'hello world'
print "hello world + 306 *5"

a = 306 * 5
print a

print 306 * 5

print 4 - 3 + 7

print 3 + 4

print 6 + 8


def add(a, b):
    print a + b


def multi(a, b):
    print a * b


def do_something(a, b, c):
    print 'a', a + b
    print 'b', c * (b - a)
    print 'c', (c + b) / a


def reverse_string(s):
    c = ''
    for g in reversed(s):
        c += g
    print c


add(3, 4)
add(6, 8)
print 10 * 8

add(6, 5)

multi(30, 6)

do_something(1, 2, 3)
do_something(6, 3, 2)
do_something(7, 3, 2)

reverse_string("hello amy!")
reverse_string("ohey evan ;|")


def calculate_number_of_atoms_in_item(item):
    am = id(item) << 64
    atoms = am / 2
    return atoms


b = calculate_number_of_atoms_in_item('amys face')
print 'there are', b, 'atoms in amys face'
