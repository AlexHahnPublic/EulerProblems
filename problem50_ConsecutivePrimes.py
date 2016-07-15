# Euler Problem 50:
# The prime 41, can be written as the sum of six consecutive primes:
#           41 = 2 + 3 + 5 + 7 + 11 + 13
# This is the longest sum of consecutive primes that adds to a prime below
# one-hundre.
# The longest sum of consecutive primes below one-thousand that adds to a
# prime, contains 21 terms, and is equal to 953.
# Which prime, below one million, can be written as the sum of the most
# consecutive primes?

# Solution
# ---------------------------------------------------------
#   1) First we can generate all primes below 1 million. Although it would probably
#   be very safe to just generate all the primes below 500,000 (maybe even
#   250,000) since we're probably not going to find too many longer chains 
#   of consecutive primes that add to a number below one million. We can make
#   this optimization later if necessary.  AFter running with input one
#   million, we will have to lower the upper bound.
#   2) Next we can generate all possible sums of all possible
#   consecutive sets. The best way to do this is with a "sliding window"
#   approach. First we'll find all the length two sums, then length three,
#   etc. We can create a record that will store the resulting sum and number
#   of prime pairs if the sum is below 1 million.
#   3) Lastly we can start at the highest length sum numbers and check
#   primality until we find the first that is a prime

import time as T

def main(num):
    st = T.time()
    primes = sieveOfEratosthenes(num)
    print "primes calculated, len is:", len(primes)
    lensSums = lstOfLensAndSums(primes)
    print "all lengths and sums calculated, len is:", len(lensSums)
    ind = len(lensSums)-1
    print "ind decided"
    found = False

    while not found:
        #print "Checking", lensSums[ind]
        if isPrime(lensSums[ind][1]):
            ans = lensSums[ind][1]
            found = True
        ind -= 1
    tt = T.time()-st
    print "The largest prime under", num, "that can be written as the sum of the most consecutive primes is", ans
    print "This program took", tt, "Seconds to run"

def sieveOfEratosthenes(n):
    size = n//2
    sieve = [1]*size
    limit = int(n**0.5)
    for i in range(1,limit):
        if sieve[i]:
            val = 2*i+1
            tmp = ((size-1) - i)//val 
            sieve[i+val::val] = [0]*tmp
    return [2] + [i*2+1 for i, v in enumerate(sieve) if v and i>0]

def lstOfLensAndSums(lst):
    lensSums = []
    window = 2 # Let's create the list from biggest to smallest

    while window <= len(lst):
        for start in range(len(lst)-window+1):
            sum =0
            for i in range(start,start+window):
                sum += lst[i]
            if sum < 1000000: # don't want sums over a million
                lensSums.append((window,sum))
        window += 1
    return lensSums

def isPrime(num):
    i = 2
    boolVal = True
    while i*i <= num and boolVal == True:
        if num%i == 0:
            boolVal = False
        else:
            i += 1
    return boolVal


if __name__ == "__main__":
    import sys
    #sieveOfEratosthenes(int(sys.argv[1]))
    #a = [x for x in range(1000)]
    #print lstOfLensAndSums(a)
    #isPrime(int(sys.argv[1]))
    main(int(sys.argv[1]))

