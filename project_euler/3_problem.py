"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

#http://stackoverflow.com/questions/9816603/range-is-too-large-python
def prime_factors(x):
    factors = []
    #2 is the only even prime factor, so remove all even factors
    while x % 2 == 0:
        factors.append(2)
        x /= 2

    i = 3
    #no factors can be larger than the squareroot of the number
    while i <= int(x**0.5):
        while x % i == 0:
            x/=i
            factors.append(i)
        i += 2 #check only odd numbers
    if x > 1:
        factors.append(x)

    return factors

print prime_factors(600851475143)[-1]
