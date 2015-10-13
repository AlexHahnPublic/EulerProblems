# Euler Problem 30:
# Surprisingly there are only three numbers that can be written as the sum of
# fourth powers of their digits:

#      1634 = 1^4 + 6^4 + 3^4 + 4^4
#      8208 = 8^4 + 2^4 + 0^4 + 8^4
#      9474 = 9^4 + 4^4 + 7^4 + 4^4

# As 1 = 1^4 is not a sum it is not included

# The sum of these numbers is 1634 + 8208 + 9474 = 19316

# Find the sum of all the numbers that can be written as the sum of fifth
# powers of their digits.

# Solution:
#------------------------------------------------

# I can't think of number theoretic way to go about this, will check each
# number. We must analytically find some upper bound to finish the search

# We can see that the sum of the largest 5 digit number with each number
# raised to the fifth is 9^5+9^5+9^5+9^5+9^5=5*9^5=295245. So with 5 digits we
# can make a 6 digit number 6*9^5=354294 so 355000 seems like a reasonable
# bound. TODO: make functional, this will require a writing a simple
# subfunction to calculate an upper bound

import time as T

def DigitNthPower():
    st = T.time()
    upperBound=6*(9**5)
    total=0
    for i in range(10,upperBound+1):
        sumDigs=0
        for c in str(i):
            sumDigs+=int(c)**5
        if sumDigs==i:
            total+=i
    tt = T.time()-st
    print "The sum of all the numbers who's sum of its digits raised to the 5th power equal the number itself is:", total
    print "This program took", tt, "seconds to run"
    
            
if __name__=="__main__":
    #import sys
    DigitNthPower()
