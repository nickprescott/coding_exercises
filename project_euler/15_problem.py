"""
Starting in the top left corner of a 2x2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20x20 grid?
"""
grid_size = 20
node_count = (grid_size + 1)**2

def create_path_count_map(node_count):
    """
    Given a 2x2 grid with nodes:
    ABC
    DEF
    GHI
    The sum of paths to I is equal to the paths to F + paths to H.
    E = B+D, etc.
    A=B=C=D=G = 1.
    """
    nodes = {}
    for x in range(1, node_count+1):
        if x <= (node_count**0.5):#first row can only be reached by one path
            nodes[x] = 1
        elif x % (node_count**0.5) == 1: #first column can only be reached by one path
            nodes[x] = 1
        else:
            nodes[x] = nodes[x-1] + nodes[x - (node_count**0.5)]

    return nodes
        
print create_path_count_map(node_count)[node_count]
