# Euler Problem 53:
# There are exactly ten ways of selecting three from five, 12345:
#   123, 124, 125, 134, 135, 145, 234, 245, 345
# In combinatorics, we use the notation 5C3 = 10
# In general,
#   nCr = (n!)/(r!(n-r)!), where r <= n, n! = n x (n-1) n ... x 2 x 1, and 0!=1
#   by convention
# It is not until n = 23, that a value exceeds one-million: 23 C 10 = 114406.
#
# How many, not necessarily distinct, values, of nCr, for 1<=n <= 100, are
# greater than one-million?

# Solution:
# ---------------------------------------------------------
# This is another fairly straight forward problem in my opinion. To solve we'd
# simply need to write a simple choose function (nice not to use the
# built-ins), then have a double for loop for n 1:100 and c 1:i keeping track of
# how many are over one million.


import time as T

def main(maxN):
    st = T.time()
    total = 0
    for n in range(maxN+1):
        for r in range(n):
            if choose(n,r)>1000000:
                #print "found one:", n, "Choose", r, "=", choose(n,r)
                total +=1
    tt = T.time() - st
    print "The number of n choose r values that come out to be greater than 10000000 (one million) for maxn =", maxN, "is:", total
    print "This program took", tt, "Seconds to run"


def factorial(num):
    if num == 0:
        total = 1
    else:
        total = num
        while num>1:
            num -= 1
            total *= num
    return total

def choose(n,r):
    return factorial(n)/(factorial(r)*factorial(n-r))


if __name__ == "__main__":
    import sys
    main(int(sys.argv[1]))

