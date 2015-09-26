# Euler Problem 5:
# 2520 is the smallest number that can be divided by each of the numbers
# from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible by all of the
# numbers from 1 to 20?

# Solution: starting at 1 and incrementing until we find a number that is
# divisible by all the numbers up to 20 is an inefficient brute force method.
# Instead let's take the prime decomposition for all of the numbers up to 20,
# then multiply together the primes necessary to form each number
# (basically the max multiplicity of each prime)
import time

# Helper Function, Compute the prime factorization of a number
def primeFactors(num):
    primeDecomp = []
    i = 2
    while i <= num:
        while num%i == 0:
            primeDecomp.append(i)
            num /= i
        i += 1
    return primeDecomp

#TODO: Finish implementing this faster prime decomp method
#better to use only up to square root prime factorization
def primeFactorsBetter(num):
    numOrig = num # to later check for sqrt case as to not double count
    primeDecomp = []
    i = 2
    while i * i < num:
        while num%i == 0:
            primeDecomp.append(i)
            num /= i
        i += 1
    primeDecomp.append(num)
    print primeDecomp



# Main Function
def smallestMultiple(n):
    orig_n = n      # Original number for printing results later
    start_time = time.time()
    toMult = []     # The collection of the prime decompositions
    countdict = {}  # a dictionary that hold {k,v]={n, prime decomp of n}

    # Create a key value dictionary with the prime decomp of each key
    for i in range(2,n+1):
        countdict[i] = primeFactors(i)  # dict of prime decomp up to n

    # construct the correct list of numbers to multiple by taking the highest
    # multiplicity of each prime factor in all the numbers up to n
    for j in countdict:     # look at each key (number up to n)
        for k in countdict[j]: # a list of each keys prime decomp
            if toMult.count(k) == 0: # if a new number (has to be prime)
                toMult.append(k)

# If the multiplicity of the prime factors of the new number is greater
# than the current greatest multiplicities, add it into the toMult list
            elif countdict[j].count(k) > toMult.count(k):
                # note that you could get away with an else, but that's
                # only because range(1,-number) = [], so no adj takes place
                # that's not clear so I'm including the condition
                for q in range(1,countdict[j].count(k)-toMult.count(k)+1):
                    toMult.append(k)

#collapse the list with multiply (if you want TODO: use an anonymous function)
    answer = 1
    for number in toMult:
        answer *= number
    total_time = time.time() - start_time
    print "The smallest number that is evenly divisible by all numbers from 1 to", orig_n, "is", answer
    print "This program took:", total_time, "seconds to run"



if __name__ == "__main__":
    import sys
    smallestMultiple(int(sys.argv[1]))
    #primeFactorsBetter(int(sys.argv[1]))
