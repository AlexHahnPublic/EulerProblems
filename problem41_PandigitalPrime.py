# Euler Problem 40:
# We shall say that an n-digit number is pandigital if it makes use of all the
# digits 1 to n exactly once. For example, 2143 is a 4-digit
# pandigital and is also prime.
#
# What is the largest n-digit pandigital prime that exists?

# Solution:
# Well we can provide a very logical/cursory upperbound of 987654321 since
# any number bigger than that can't be pandigital. We can then think about
# the sum of the digits of each length pandigital number:

# P(2) = 1+2 = 3
# P(3) = 1+2+3 = 6
# P(4) = 1+2+3+4 = 10
# P(5) = 1+2+3+4+5 = 15
# P(6) = 1+2+3+4+5+6 = 21
# P(7) = 1+2+3+4+5+6+7 = 28
# p(8) = 1+2+3+4+5+6+7+8 = 36
# P(9) = 1+2+3+4+5+6+7+8+9 = 45

# Since permuting the numbers around won't change the sum (addition is
# commutative) this is a good way to use a little number theory to really
# do some damage and greatly reduce the solution space. We can easily see that
# all N-digit pandigitals other than length 7 and 4 have sum digits that are
# divisible by three. This means that all the permutations of those length
# pandigitals will all be divisible by 3 and therefore not prime.

# I think a very natural logical progression to think of is to generate primes then
# check if they're pandigital and take the largest one. But now knowing that they'll only be length 4
# or 7 and that there are 7!=5040 ways to order 7 items and 4!=24 ways to order
# 4 items giving us a total of only 5064 numbers to check, we start to feel
# that generating pandigitals \it{then} checking primality might be the way
# to go.

# Lastly to top it off we know that the largest 7 digit pandigital number
# is 7654321. If we permute wisely and take the next largest 7 digit
# pandigital number each step then we only need to proceed until we find the
# first prime number!

import time as T

def LgPanPrime():
    start = "7654321"


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


if __name__ == '__main__':
    import sys
    #lst= Heaps(3,[1,2,3,4,5])
    val=isPrime(int(sys.argv[1]))
    print val


