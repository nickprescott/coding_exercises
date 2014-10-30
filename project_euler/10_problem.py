"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""
primes = []
def generate_primes(limit):
    yield 2
    yield 3
    potential_prime = 5
    yield potential_prime
    potential_prime += 2

    while potential_prime < limit:
        if is_prime(potential_prime):
            yield potential_prime
        potential_prime +=2

def is_prime(value):
    for x in primes:
        if x > (value**0.5 +1):
            return True
        if value % x == 0:
            return False
    return True

def prime_factors_list_method(limit):
    total = 0
    for x in generate_primes(limit):
        primes.append(x)
        total += x 

    return total

#print prime_factors_list_method(2000000)


#much faster
def sieve_method(limit):
    sieve = [True]*limit
    potential_prime = 3
    total = 2
    while potential_prime < limit:
        if sieve[potential_prime]:
            total += potential_prime
            multiple = potential_prime
            while multiple < limit:
                sieve[multiple] = False
                multiple += potential_prime
        potential_prime += 2
    return total

#print sieve_method(2000000)


#optimized with better marking of multiples and cut down the iterations
#by reasoning about factors above the square root of the max
def sieve_method_2(limit):
    sieve = [True]*limit
    potential_prime = 3
    #numbers greater than the square root of the max are either prime or have already been factored out, so we don't need to test them
    while potential_prime < (limit**0.5 +1):
        if sieve[potential_prime]:
            multiple = potential_prime
            #remove multiples of the prime from the sieve
            sieve[multiple*2::multiple] = [False] * ((limit-1)/multiple -1)
        potential_prime += 2
    #add 2 to the list of primes left in the sieve
    return [2] + [x for x in xrange(3, limit, 2) if sieve[x]]

print sum(sieve_method_2(2000000))
