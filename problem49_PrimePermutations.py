# Euler Problem 49:
# The arithmetic sequence 1487, 4817, 8147, in which each of the terms
# increases by 3330, is unusual in two ways: (i) each of the three terms
# are prime, and, (ii) each of the 4-digit numbers are permutations of one
# another.
#
# There are no arithmetic sequences made up of three, 1-, 2-, or 3-digit
# primes, exhibiting this property, but there is one other 4-digit
# increasing sequence.
#
# What 12-digit number do you form by concatenating the three terms in this
# sequence?

# Solution:
# ---------------------------------------------------------
# I believe that a straightforward, step by step approach, might be easier
# than trying to tackle some prime/permutation number theoretic shortcut
# (I don't believe it is a coincidence that the above example have terms
# that all end in 7 however! Also the fact that the arithmetic sequence
# has a common difference of 3330 is no mistake/ random chance as well,
# this has to do with keeping the primes in the same
# equivalence/congruence class but once again, this problem is easy enough
# to solve first just with a straightforward program). 
# The steps are as follows:
#   1) Generate all primes less than 10000. This isn't to bad, using
#   pi(10000)~ 10000/log 10000 ~ 1086. Chopping off the primes with less
#   than four digits as well we are left with a list <1000 in length.
#   2) Starting with the first prime, permute its digits all 4!=24 ways.
#   Check primality of each permutation and store the primes in a list.
#   Additionally this list should be uniqued (made into a set) to avoid
#   lists like [7777, 7777, 7777, ..., 7777].
#   3) Calculate the distances between all the primes in that list. This
#   will be a length sum(1:n-1) list. Note that this is not too big, at most
#   it would be a length sum(1:24) list and that would be only if all
#   permutations of the digits were prime which is extremely
#   improbable (and maybe impossible but that's beyond checking here).
#   4) Lastly starting at the first entry in the primePermutations we add
#   TWICE the distances in the Cartesian product sense, if that number is also
#   in the primePermutations list then we've found our answer (note that
#   there are two arithmetic progressions altogether, so we can exit after
#   finding both).
# 
# Sounds complicated but it's really not if we break it down
# appropriately! We can make a few number theoretic assertions later if the
# search space/ run time seems to be too large.

import time as T
import itertools

def main(lim):
    st = T.time()
    primes = allPrimesBelow(lim)
    eligiblePrimes = dropBelow1000(primes)
    sols= [] # Need to find two sequences
    ind = 0 # I'd rather not use break statements so I'll loop through the
    # eligiblePrimes list by incrementing the index (ind) until I find the
    # answer, and change the found flag to True

    while len(sols) < 2: # there are two arithmetic progressions! One's given!

        # Generate the list of all digit permutations of the prime
        perms = set(list(map("".join, itertools.permutations(str(eligiblePrimes[ind])))))

        # Throw out all the non prime permutations
        primePerms=[]
        for i in perms:
            if isPrime(int(i)):
                primePerms.append(int(i))

        # Sort and drop primes <1000
        primePermsG1000 = sorted([x for x in primePerms if x>1000])
        l = len(primePermsG1000)
        # If there are 3 or more primes > 1000 left calculate all
        # distances between them
        dists = []
        if l >= 3:
            for i in range(l):
                for j in range(i+1,l):
                    if primePermsG1000[i]+(2*(abs(primePermsG1000[j]-primePermsG1000[i]))) in primePermsG1000:
                        if str(primePermsG1000[i])+str(primePermsG1000[j])+str(primePermsG1000[i]+(2*(abs(primePermsG1000[j]-primePermsG1000[i])))) not in sols:
                            sols.append(str(primePermsG1000[i])+str(primePermsG1000[j])+str(primePermsG1000[i]+(2*(abs(primePermsG1000[j]-primePermsG1000[i])))))
        ind += 1
    tt = T.time() - st
    print "The two arithmetic sequences (at least three in length) whose elements are permutations of the same digits, and are all prime are (concatenated together as the problem asks):", sols[0], sols[1]
    print "This program took", tt, "seconds to run"
   
def dropBelow1000(lst):
    newlst = []
    for num in lst:
        if num >= 1000:
            newlst.append(num)
    return newlst

def allPrimesBelow(n):
    notPrime = []
    primes = []
    for num in range(2,n+1):
        if num not in notPrime:
            primes.append(num)
            for mults in range(num*num, n+1, num):
                notPrime.append(mults)
    return primes

def isPrime(num):
    i = 2
    boolVal = True
    while i*i <= num and boolVal == True:
        if num%i ==0:
            boolVal = False
        else:
            i += 1
    return boolVal

if __name__ == "__main__":
    import sys
    main(int(sys.argv[1]))
