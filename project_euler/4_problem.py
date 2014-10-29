"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.
Find the largest palindrome made from the product of two 3-digit numbers.
"""
palindrome = 0

def is_palindrome(value):
    return value == value[::-1]

for x in xrange(999, 99, -1):
    for y in xrange(999, 99, -1):
        product = x*y
        if is_palindrome(str(product)):
            if product > palindrome: 
                palindrome = product
            break

print palindrome

