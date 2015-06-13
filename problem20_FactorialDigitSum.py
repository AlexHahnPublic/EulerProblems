# Euler Problem 20:
# n! means nx(n-1)x...x3x2x1
# For example, 10! = 10x9x8x7x6x5x4x3x2x1 = 3628800,
# and the sum of the digits in the number 10! is 3+6+2+8+8+0+0 =27.

# Find the sum of the digits in the number 100!

import math as M
import time as T

def factSum(n):
    start_time = T.time()
    total = 0
    strInt = str(long(M.factorial(100)))
    for dig in strInt:
        total += int(dig)
    total_time = T.time() - start_time
    print "the total of the sum of the digits in", n, "factorial is:", total
    print "This program took", total_time, "seconds to run"

# Anonymous functions are handy
def oneLiner(n):
    print reduce(lambda x, y: x+y, [int(i) for i in str(reduce(lambda x, y: x *y, range(1,n)))])

# using one anonymous function and math module
def oneLiner2(n):
    print reduce(lambda x, y: x+y, [int(i) for i in str(M.factorial(n))])

if __name__ == "__main__":
    import sys
    factSum(int(sys.argv[1]))
