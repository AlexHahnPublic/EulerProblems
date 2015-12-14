# Euler Problem 37:
# The number 3797 has an interesting property. Being prime itself, it is
# possible to continuously remove digits from left to right, and still reamain
# prime at each stage: 3793, 797, 97, and 7. Similarly we can work from right
# to left: 3797, 379, 37, and 3.
# Find the sum of the only eleven primes that are both truncatable form left to
# right and right to left.
#
# NOTE: 2, 3, 5, and 7, are not considered to be truncatable primes.

import time as T

def truncateLeft(num):
    return int(str(num)[1:])

def truncateRight(num):
    return int(str(num)[:-1])


def filterCodintions(num):




def main(inp):
    print "input is:", inp
    print "truncateLeft produces:", truncateLeft(inp)
    print "truncateRight produces:", truncateRight(inp)

if __name__ == "__main__":
    import sys
    main(int(sys.argv[1]))

