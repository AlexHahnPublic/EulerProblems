# Euler Problem 27:
# Euler discovered the remarkable quadratic formula:
#       n^2+n+41
# It turns out that the formula will produce 40 primes for the
# consecutive values of n=0 to 39. However, when n=40,
# 40^2+40+41=40(40+1)+41 is divisible by 41, and certainly when n=41,
# 41^2+41+41 is clearly divisible by 41.

# The incredible formula n^2-79n+1601 was discovered, which produces 80
# primes for the consecutive values n = 0 to 79. The product of the
# coefficients, -79 and 1601 is -126479/

# Considering quadratics of the form:

#       n^2+an+b, where |a|<1000 and |b|<1000
#       where |n| is the modulus/absolute value of n
#       e.g. |11|=11 and |-4|=4

# Find the product of the coefficients, a and bm for the quadratic 
# expression that produces the maximum number of primes for consecutive values
# of n, starting with n=0.

# Solution:
#------------------------------------------------
# Generally finding functions that generate primes is not a simple task
# (collect some bit coin if you have some good ones!). I think the only way
# I can think of to go after this problem is brute force on a reduced solution
# space:

# Reduction 1:
# when n=0 we just have b, since we're going with the standard
# definition of primes we can now limit b to be a positive prime. We could
# generate the list of primes under 1001 using a sieve and iterate through
# that list but I'd rather just leverage our isPrime function as much as
# possible

# Reduction 2: for n=1 we have 1+a+b, therefore a> (-b+1)
# a must be an odd negative number (We can validly assume b won't be 2) and b ranges
# from -(a+1) to 1000

# Coming back to it we can guaruntee that b won't be two because if it was then we
# would could only generate primes for n=0,1, then 2 would be a composite because
# 2^2 + a(2)+2 is divisible by 2, we know that the chain is longer than 2 already

import time as T

# Our fast isPrime function
def isPrime(n):
    if n<2: return False
    if n==2: return True
    if n==3: return True
    if n%2==0: return False
    if n%3==0: return False
    i=5
    w=2
    while i*i<=n:
        if n%i==0:
            return False
        i+=w
        w=6-w
    return True

def quadraticPrimes(n):
    start_time=T.time()
    maxLenPrimes = 0
    maxCoeffs = (0,0)
    for a in range(-n+2, 0, 2):
        for b in range(-a, n-1, 2):
            x = 1
            while isPrime(x**2+a*x+b):
                x += 1
            if x > maxLenPrimes:
                maxLenPrimes = x
                maxCoeffs = (a,b)
    total_time=T.time() - start_time
    print "The quadratic that gives the longest sequence of primes for consecutive integer inputs starting at 0 is: n^2 +", maxCoeffs[0],"n +", maxCoeffs[1], ", with coefficients reading off as a =", maxCoeffs[0], "and b =", maxCoeffs[1],". This quadratic gives", maxLenPrimes+1, "primes in a row for inputs 0 to", maxLenPrimes, ". The coefficients' corresponding multiplication is:", maxCoeffs[0]*maxCoeffs[1]
    print "This program took", total_time, "seconds to run"

if __name__=="__main__":
    import sys
    quadraticPrimes(int(sys.argv[1]))
