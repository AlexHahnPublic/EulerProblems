# Euler Problem 23:
# A perfect number is a number for which the sum of its proper divisors is
# exactly equal to that number. For example, the sum of the proper divisors of
# 28 would be 1+2+4+7+14=28, which means 28 is a perfect number.

# A number n is called deficient if the sum of its proper divisors is less than
# n and it is called abundant if the sum exceeds n.

# As 12 is the smallest abundant number, 1+2+3+4+6=16, the smallest number that
# can be written as the sum of two abundant numbers is 24. By mathematical
# analysis, it can be shown that all integers greater than 28123 can be written
# as the sum of two abundant numbers. However, this upper limit cannot be
# reduced any further by analysis even though it is known that the greatest
# number that cannot be expressed as the sum of two abundant numbers is less
# than this limit. Fin the sum of all the positive numbers which cannot be
# written as the sum of two abundant numbers.

# Solution: We only need to find all the abundant numbers less than 28123 since
# we know that any number over that can be written as the sum of two abundant
# numbers. We will create a list of all the abundant numbers then form another
# list of all the possible sums of two of those numbers. Then we will drop any
# number greater than 28123 (no real reason to check) and take the complement
# of that set with all positive numbers less than 28123.


import time as T

# Sum the proper divisors of a number n
def sumDivisors(n):
    total = 1
    sqrt = n**.5
    divisor=2
    while divisor <= sqrt:
        if n % divisor ==0:
            total += divisor + n/divisor
        divisor += 1
    if n**.5%1==0:
        total -= int(sqrt)
    return total

# calculate all of the pair sums of a list (can add element to itself), return
# a set (no duplicates)
def allSums(lst):
    sums=[]
    for i in range(len(lst)):
        for j in range(i,len(lst)):
            sums.append(lst[i]+lst[j])
    mySet=set(sums)
    return mySet


def nonAbundantSums(num):
    st=T.time()
    abunNums=[]
    for i in range(1,num+1):
        if sumDivisors(i)>i:
            abunNums.append(i)
    sumOf2AbunNums=allSums(abunNums)
    total=0
    for j in range(1,num+1):
        if j not in sumOf2AbunNums:
            total += j
    tt=T.time()-st
    print "The sum of all numbers that cannot be expressed as the sum of two abundant numbers is:",total
    print "This program took", tt, "seconds to run"



if __name__=="__main__":
    import sys
    nonAbundantSums(int(sys.argv[1]))


