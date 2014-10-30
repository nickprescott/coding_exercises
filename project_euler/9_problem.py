"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""
for a in xrange(1, 500):
    for b in xrange(1, 500):
        if (a**2 + b**2) == (1000 - a - b)**2:
            print a*b*(1000-a-b)
            exit() 
