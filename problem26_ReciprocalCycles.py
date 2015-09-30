# Euler Problem 26:
# A unit fraction contains 1 in the numerator. The decimal
# representation of the unit fractions with denominators 2 to 10 are given:

#   1/2 = 0.5
#   1/3 = 0.(3)
#   1/4 = 0.25
#   1/5 = 0.2
#   1/6 = 0.1(6)
#   1/7 = 0.(142857)
#   1/8 = 0.125
#   1/9 = 0.(1)
#   1/10 = 0.1

# Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can
# be seen that 1/7 has a 6-digit recurring cycle.

# Find the value of d < 1000 for which 1/d contains the longest
# recurring cycle in its decimal fraction part.

#Solution
#--------------------------------------------------------------------

# It's fairly straightforward to show that the decimal expansion for 1
# over a number terminates if the number can be factored into 
# multiples of 2's# and 5's:

#       finite decimal expansion iff 1/n = 1/(2^x5^y)

# we can see that all numbers relatively prime to 10 will immediately start
# its periodic decimal expansion. The only numbers that are left are numbers
# that have at least one factor 2 or 5 in them and also have at least one non
# 2 or 5 factor.

#The period of the decimal expansion for a non terminating expansion can be
# found by looking at the multiplicative order of its denominator

# The period for the nonterminating decimal expansion can be found by solving
# the discrete logarithm $10^s\equiv 10^{s+t}(mod n)$

# An intuitive sense of this that the multiple of 10 terms will mod out to 0
# mod 10 s times and the rest of the terms will form the residual group of
# the leftover number relatively prime to 10 with a period of t

#QUICK EXAMPLE n=84

# 10^0\equiv 1 (mod 84), 10^1\equiv 10 (mod 84), 10^2\equiv 16 (mod 84)
# 10^3\equiv -8 (mod 84), 10^4\equiv 4 (mod 84), 10^5\equiv 40 (mod 84)
# 10^6\equiv -20 (mod 84), 10^7\equiv -32 (mod 84), 10^8\equiv 16 (mod 84)

# Therefore we can see that the first 2 terms will be the non
# repeating part of the decimal expansion (t=2) and the remaining 6 terms
# form the length of the period (s=6)

# However we can see from here that we only really need to look at the primes
# (outside of 2 and 5 because the non repeating part of the decimal is 
# irrelevant to the period of the cyclic decimal expansion

# We are left solving the discrete logarithm 10^k\equiv 1(mod n) (a
# difficult problem for large n (useful in crypotography (unless you maybe
# have a quantum computer and some Qbits at your disposal (see Shor's
# Algorithm)))

import time as t

def longestPeriod(n):
    start_time = t.time()
    #Find the list of primes under n:
    for i in Sieve(n)[::-1]:
        per = 1
        while pow(10, per, i) != 1:
            per += 1
        if i-1 == per:
            break
    total_time = t.time()-start_time
    print "longest period for numbers 1/1...",n," is: ", i
    print "This program took", total_time, "seconds to run"


def Sieve(n):
    primes = []
    notPrimes = []
    for i in xrange(2,n+1):
        if i not in notPrimes:
            primes.append(i)
            for j in xrange(i*i, n+1, i):
                notPrimes.append(j)
    return primes



#TODO: FIX
# Helper function to return the all the primes under some number n
#def SieveOfEratoshenes(n):
#    vals = [True] * n
#    vals[0] = vals[1] = False
#    for (i, isPrime) in enumerate(vals):
#        print i
#        if isPrime:
#            yield i
#            for n in xrange(i*i, n, i):
#                vals[n] = False
#    print vals

# Is prime helper function
#def isPrime(n):
#    if n==2 or n==3:
#        return True
#    if n%2==0 or n<2:
#        return False
#    for i in range(3,int(n**.5)+1,2): #(only check odds)
#        if n%i==0:
#            return False
#    return True


if __name__ == "__main__":
    import sys
    longestPeriod(int(sys.argv[1]))

