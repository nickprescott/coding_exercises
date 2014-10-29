"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

def is_divisible(value):
    for i in xrange(11, 20):
        if value % i != 0:
            return False
    return True

#2520 is divisible by 1,10 but not by 11, so start there
counter = 2520
while True:
    if is_divisible(counter):
        break
    #increment by 2520 since this will cover numbers that are divisible by 1-10
    #so you can just check 11-20
    counter += 2520

print counter
