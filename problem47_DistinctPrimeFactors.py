# Euler Problem 5:
# The first two consecutive numbers to have two distinct prime factors are:
#       14 = 2 x 7
#       15 = 3 x 5
#
# The first three consecutive numbers to have three distinct prime factors are:
#       644 = 2^2 x 7 x 23
#       645 = 3 x 5 x 43
#       646 = 2 x 17 x 19
#
# Find the first four consecutive integers to have four distinct prime factors.
# What is the first of these numbers?

# Solution:
#----------------------------------------------------------
# starting at 1 (because the 2 and 3 case has no bearing on the 4 case)
# generate the prime factors of each next number, start a count when you get
# one that equals 4, if the next three also have four then return the first
# number, else continue with the while loop

import time as T

def primeFactors(num):
    primeFacs = []
    d = 2
    while d*d <= num:
        while (num % d) == 0:
            primeFacs.append(d)
            num//=d
        d+=1
    if num >1:
        primeFacs.append(num)
    return list(set(primeFacs))

def main():
    st = T.time()
    found = False
    start = 2
    while not found:
        if len(primeFactors(start))==4:
            if len(primeFactors(start+1))==4 and len(primeFactors(start+2))==4 and len(primeFactors(start+3))==4:
                ans = start
                found = True
            else:
                start+=1
        else:
            start+=1
        tt = T.time()-st
    print "The first integer of the first four integers to have four distinct prime factors is:", ans
    print "This program took", tt, "seconds to run"



if __name__ == "__main__":
    import sys
    #primeFactors(int(sys.argv[1]))
    main()


