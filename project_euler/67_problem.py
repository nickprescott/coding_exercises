"""
By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom in triangle.txt (right click and 'Save Link/Target As...'), a 15K text file containing a triangle with one-hundred rows.

NOTE: This is a much more difficult version of Problem 18. It is not possible to try every route to solve this problem, as there are 2^99 altogether! If you could check one trillion (10^12) routes every second it would take over twenty billion years to check them all. There is an efficient algorithm to solve it. ;o)
"""
def create_triangle(data_file):
    triangle = []
    with open(data_file, 'rb') as data:
        for line in data:
            digit_list = map(int, line.split())
            triangle.append(digit_list)
    
    return triangle

def sum_from_the_bottom(triangle):
    """
    sum the elements in the path starting from the bottom of the triangle.
    compare two elements and choose the larger to add to the next element
    """
    triangle = list(reversed(triangle))
    height = len(triangle) -1
    for x,row in enumerate(triangle):
        for y, value in enumerate(row):
            if y > len(row) -2:#last item in a row has already been checked
                break
            if x+1 > height:#last row is the answer
                break
            #set the next value in the path to be the sum of the greater of the two
            triangle[x+1][y] += max([value, row[y+1]])
    return triangle[height][-1] # 'top' of the triangle is the answer

print sum_from_the_bottom(create_triangle('problem_67_triangle.txt'))
