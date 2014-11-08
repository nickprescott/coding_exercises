"""
Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

    21 22 23 24 25
    20  7  8  9 10
    19  6  1  2 11
    18  5  4  3 12
    17 16 15 14 13

    It can be verified that the sum of the numbers on the diagonals is 101.

    What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?
"""
diagonal_sum = 0
next_diagonal_incrementor = 2
x=1

while x <= 1001**2:
    diagonal_sum += x
    x += next_diagonal_incrementor
    if x % (x**0.5) == 0:
        next_diagonal_incrementor +=2

print diagonal_sum
