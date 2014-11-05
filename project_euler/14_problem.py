"""
The following iterative sequence is defined for the set of positive integers:

    n -> n/2 (n is even)
    n -> 3n + 1 (n is odd)

    Using the rule above and starting with 13, we generate the following sequence:
    13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""
import functools

def collatz_count(num):
    if num not in collatz_count.store:
        if num == 1:
            collatz_count.store[num] = 1
        elif num%2 == 0:
            collatz_count.store[num] = collatz_count(num/2) + 1
        else:
            collatz_count.store[num] = collatz_count(num*3+1) + 1

    return collatz_count.store[num]

collatz_count.store = {}

class Memoize(object):

    def __init__(self, function):
        self.function = function
        self.store = {}

    def __call__(self, *args):
        if not args in self.store:
            self.store[args] = self.function(*args)
        return self.store[args]

def memoize(obj):
    cache = obj.cache = {}

    @functools.wraps(obj)
    def memoizer(*args, **kwargs):
        key = str(args) + str(kwargs)
        if key not in cache:
            cache[key] = obj(*args, **kwargs)
        return cache[key]
    return memoizer

@memoize
def collatz_count2(num):
    if num == 1:
        return 1
    elif num%2 == 0:
        return collatz_count2(num/2) + 1
    else:
        return collatz_count2(num*3+1) + 1

print max(collatz_count(x) for x in xrange(2, 1000000)) #fastest
#print max(collatz_count2(x) for x in xrange(2, 1000000)) #second place

#not sure why using the Memoize class as a decorator produces a recursion limit error. @Memoize should be equivalent to collatz_count2 = Memoize(collatz_count2)
#c = Memoize(collatz_count2)
#print max(c(x) for x in xrange(2, 1000000)) #last
