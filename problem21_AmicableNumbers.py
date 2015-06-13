# Euler Problem 20:
# Let d(n) be defined as the sum of proper divisors of n (numbers less than n
# that divide evenly into n). if d(a)=b and d(b)=a, where a not equal b, then a
# and b are an amicable pair and each of a and b are called amicable numbers.

# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44,
# 55, and 110; therefore d(220)=284. The proper divisors of 284 are 1, 2, 4,
# 71, and 142; so d(284)=220.

# Evaluate the sum of all the amicable numbers below 10000.

import time as T

def sumOfProperDivisors(n):
    total = 1
    for i in range(2,int(n**.5)+1):
        if n%i==0:
            total += i+n/i
    if n**.5%1==0:
        total -= n**.5
    return int(total)

# Greedy algotithm. Not too bad runtime though. Note that if we find amicable
# numbers a and b we shouldn't then later check if b is an amicable number, but
# these numbers aren't too dense. If we want we could keep a record of amicable
# numbers found and make sure before we check if a number is amicable that it
# is not already in the record.

def sumOfAmicableNumbers(n):
    start_time = T.time()
    total=0
    for i in range(2,n+1):
        b=sumOfProperDivisors(i)
        if b<n and b!=i and sumOfProperDivisors(b)==i:
            print "found an amicable number:", i
            total += i
    total_time = T.time()-start_time
    print "The sum of all amicable numbers under", n,"is", total
    print "This program took", total_time, "seconds to run"


if __name__=="__main__":
    import sys
    sumOfAmicableNumbers(int(sys.argv[1]))

