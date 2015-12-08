# Euler Problem 34:
# 145 is a curious number, as 1!+4!+5! = 1+24+120 = 145
#
# Find the sum of all numbers which are equal to the sum of the
# factorial of their digits.
#
# Note: as 1!=1 and 2!=2 are not sums, they are not included

# Solution:
# We can start by finding an upper bound by noting that for n a natural
# number of d digits, 10d-1<=n<=9!d fails do hold for any d>=8. So the maximum
# sum of factorials of digits for a 7 digit number is 9!*7=2,540,160
# We can now cash the factorials 1!-9! and brute force check for n \in
# [10,2540160]:

import time as T
import math as M

facts=[1, 1, 2, M.factorial(3), M.factorial(4), M.factorial(5),
            M.factorial(6), M.factorial(7), M.factorial(8),
            M.factorial(9)]

def digFacts(upper):
    st = T.time()
    global facts
    sum = 0
    for i in range(10, upper+1):
        if sumDigFacts(i):
            print "found one", i
            sum += i
    tt = T.time() - st
    print "The sum of all numbers which can be written as the sum of their factorial digits is:", sum
    print "This program took", tt, "seconds to run"

def sumDigFacts(num):
    strRep=str(num)
    sum = 0
    for i in strRep:
        sum += facts[int(i)]
    if sum == num:
        return True
    else:
        return False



            

if __name__ == "__main__":
    import sys 
    digFacts(int(sys.argv[1]))
