"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""
primes = [2]

def odds():
    x = 3
    yield x
    while True:
        x += 2
        yield x

def is_prime(value):
    """
    every number can be written as the product of 1 or more prime numbers, so we
    only need to check the value against our known list of primes.
    """
    for x in primes:
        """
        if we check the primes less than the square root of the value first, and none are factors 
        of it, then we know that no values larger than the square root can be factors 
        of it either. So then we know the value is prime.
        """
        if x > value**0.5:
            return True
        if value % x == 0:
            return False
    return True

def find_the_prime(value):
    for x in odds():
        if is_prime(x):
            primes.append(x)
            if len(primes) == value:
                return primes[-1]
                
print find_the_prime(10001)
