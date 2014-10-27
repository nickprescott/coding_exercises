#!/usr/bin/env python
"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""
def list_comp():
    print sum([num for num in xrange(1000) if (num%3==0 or num%5==0)])

#faster for larger inputs
def with_set():
    print sum(set(xrange(0,1000,3)) | set(xrange(0,1000,5)))

list_comp()
with_set()
