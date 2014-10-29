"""
Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

    1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
"""

def fib_gen(stop_value):
    a,b = 0,1
    yield a
    yield b
    while b <= stop_value:
        a,b = b, a+b
        yield b

print sum((x for x in fib_gen(4000000) if x%2==0))
