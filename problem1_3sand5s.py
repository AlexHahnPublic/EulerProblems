# Euler Problem 1:
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we
# get 3, 5, 6, and 9. The sum of these multiples is 23

# Find the sum of all the multiples of 3 and 5 below 1000.

# Solution: trial division, check each number up to n, if divisible by 3 or 5
# add it to the running total

import time

def sum3and5(n):
    start_time = time.time()
    total = 0
    for nat in range(n):
        if (nat % 3 == 0) or (nat % 5 == 0):
            total = total + nat
    total_time = time.time() - start_time
    print "The sum of all the multiples of 3 and 5 below", n, "is", total
    print "This program took:", total_time, "seconds to run"

if __name__ == "__main__":
    import sys
    sum3and5(int(sys.argv[1]))

