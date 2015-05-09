# Euler Problem 6:
# The sum of the squares of the first ten natural numbers is,
#       1^2+2^2+3^2+...+10^2 = 385
# The square of the sum of the first ten natural numbers is,
#       (1+2+3+...+10)^2 = 55^2 = 3025
# Hence the difference between the sum of the squares of the first ten natural
# numbers and the square of the sum is 3025 - 385 = 2640.
# Find the difference between the sum of the squares of the first one hundred
# natural numbers and the square of the sum.

import time

def difOfSquares(n):
    start_time = time.time()
    sumOfSquares = 0
    squareOfSums = 0
    for i in range(1,n+1):
        sumOfSquares += i**2
        squareOfSums += i
    squareOfSums = squareOfSums**2
    difference = squareOfSums - sumOfSquares
    total_time = time.time() - start_time
    print "The difference between the sum of the squares of the first", n, "natural number and the square of the sum is:", difference
    print " This program took:", total_time, "seconds to run"

if __name__ == "__main__":
    import sys
    difOfSquares(int(sys.argv[1]))
