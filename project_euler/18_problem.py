"""
By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom of the triangle below:

    75
    95 64
    17 47 82
    18 35 87 10
    20 04 82 47 65
    19 01 23 75 03 34
    88 02 77 73 07 63 67
    99 65 04 28 06 16 70 92
    41 41 26 56 83 40 80 70 33
    41 48 72 33 47 32 37 16 94 29
    53 71 44 65 25 43 91 52 97 51 14
    70 11 33 28 77 73 17 78 39 68 17 57
    91 71 52 38 17 14 91 43 58 50 27 29 48
    63 66 04 68 89 53 67 30 73 16 69 87 40 31
    04 62 98 27 23 09 70 98 73 93 38 53 60 04 23

    NOTE: As there are only 16384 routes, it is possible to solve this problem by trying every route. However, Problem 67, is the same challenge with a triangle containing one-hundred rows; it cannot be solved by brute force, and requires a clever method! ;o)
"""

def create_triangle(data_file):
    triangle = []
    with open(data_file, 'rb') as data:
        for line in data:
            digit_list = [int(x) for  x in line.split()]
            triangle.append(digit_list)
    
    return triangle

def route(triangle, current_row=0, start_pos=0):
    """
    Generate all possible routes
    """
    for index, value in enumerate(triangle[current_row]):
        if index < start_pos: #unreachable path
            continue
        elif index > start_pos +1: #unreachable and all indexes after this are unreachable
            break
        if current_row == len(triangle) -1: #last row of the triangle
            yield [value]
        else:
            #complete the rest of the path
            for child in route(triangle, current_row+1, index):
                yield [value] + child

#find the largest route and sum it
#print sum(max(route(create_triangle('problem_18_data.txt')), key=sum))

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

print sum_from_the_bottom(create_triangle('problem_18_data.txt'))
