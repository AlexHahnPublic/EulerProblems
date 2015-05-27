# Euler Problem 15:
# Starting in the top left corner of a 2x2 grid, and only being able to move
# to the right and down, there are exactly 6 routes to the bottom right
# corner.

# How many such routes are there through a 20x20 grid?

# Solution: this is just a combination problem. We know that to start from the
# top left and only make moves down and right we must take exactly 40 moves
# for every valid path, and of those 40, 20 must be right and 20 must be down.

# The only real question is how many combinations are there? It's simply
#       Choose(n,k) = n!/((n-k)!k!)

import time
import math as M


def numPaths(dim):
    nodes = dim+1
    print M.factorial(dim*2)/(M.factorial(dim)**2)


if __name__ == "__main__":
    import sys
    numPaths(int(sys.argv[1]))
