# Euler Problem 10:
# The sum of the primes below 10 is 2+3+5+7 = 17.

# Find the sum of all the primes below two million.

# This is my original method of using the Sieve of Eratosthenes method.
# However with large n this algorithm is very memory intensive and runs
# slow because it must generate an entire list of numbers up to n then
# constantly check to find and then remove values from that list. Works
# well for n under 1 hundred thousand. It would be more efficient to use the
# list of length n of all boolean values then run the sieve just flipping
# the non primes to false, this returns a list you can run some bitwise
# arithmetic on.

# In a very similar flavor to that please see the bottom solution

import time

def sumPrimeBelow(n):
    start_time = time.time()
    lst = range(2,n)
    index = 0
    while index != len(lst)-1:
        currPrime = lst[index]
        print "currPrime is:", currPrime
        multiplier = 2
        while currPrime*multiplier < n:
            if currPrime*multiplier in lst:
                lst.remove(currPrime*multiplier)
            multiplier +=1
        index += 1
    total_time = time.time() - start_time
    print "The sum of all of the primes below", n, "is", sum(lst)
    print "This program took", total_time, "seconds to run"

def isPrime(num):
    i = 2
    boolVal = True
    while i*i <= num and boolVal == True:
        if num%i == 0:
            boolVal = False
        else:
            i += 1
    return boolVal

# This is the solution I'm going with in the short term. It's trial division
# but is better for larger n than above because it doesn't have to run through
# almost the entire list checking for whether an element is in the list
# then find it and remove it if it is. It just adds the primes as it goes
def sumPrimeBelow2(n):
    start_time = time.time()
    sum = 0
    for i in range(2,n):
        if isPrime(i):
            sum += i
    total_time = time.time() - start_time
    print "The sum of all of the primes below", n, "is", sum
    print "This program took", total_time, "seconds to run"

# This is the most optimal solution I've seen using the Sieve of
# Eratosthenes so far, note that it skips removing all the 2's (which is the
# most memory intensive computation by far, by starting with sum =2 then
# only incrementing by 2

#Idea from Lassevk on thread
def sumPrimeBelowBest(n):
    start_time = time.time()
    marked = [0] * n
    curVal = 3
    sum = 2
    while curVal < n:   # run up to the limit
    # If still marked curVal that means we haven't taken out anything that
    # multiplies to it which means it's a new prime, add it to the total sum
        if marked[curVal] == 0:
            sum += curVal
            mult = curVal
            while mult < n: # after adding to sum take out multiples
                marked[mult] = 1
                mult += curVal
        curVal += 2
    total_time = time.time() - start_time
    print "The sum of all of the primes below", n, "is", sum
    print "This program took", total_time, "seconds to run"



if __name__ == "__main__":
    import sys
    sumPrimeBelowBest(int(sys.argv[1]))
