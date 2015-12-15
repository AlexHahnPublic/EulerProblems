# Euler Problem 37
# The number 3797 has an interesting property. Being prime itself, it is
# possible to continuously remove digits from left to right, and still reamain
# prime at each stage: 3793, 797, 97, and 7. Similarly we can work from right
# to left: 3797, 379, 37, and 3.
# Find the sum of the only eleven primes that are both truncatable form left to
# right and right to left.
#
# NOTE: 2, 3, 5, and 7, are not considered to be truncatable primes.


# Solution: brute force. We can probably right a conditions function that
# checks the number for any 1s, 2s, 4s, 5s, 6s, 8s, 9s, and 0s and skips
# any further validations to cut down some clock cycles, but it runs pretty
# fast as is (and has no potential to generalize any further since there
# are only 11 of these numbers... ie don't need it to be any more
# scalable)

import time as T

def truncateLeft(num):
    if len(str(num)) > 1:
        return int(str(num)[1:])
    else:
        return "Trying to truncate a number with <= 1 digit"

def truncateRight(num):
    if len(str(num)) > 1:
        return int(str(num)[:-1])
    else:
        return "Trying to truncate a number with <= 1 digit"

def isPrime(n):
    if n<2: return False
    if n==2: return True
    if n==3: return True
    if n%2==0: return False
    if n%3==0: return False
    i=5
    w=2
    while i*i<=n:
        if n%i==0:
            return False
        i+=w
        w=6-w
    return True

def checkLeftTruncNum(num):
    while len(str(num)) > 1:
        if isPrime(num):
            num = truncateLeft(num)
        else:
            return False
    return isPrime(num)

def checkRightTruncNum(num):
    while len(str(num)) > 1:
        if isPrime(num):
            num = truncateRight(num)
        else:
            return False
    return isPrime(num)


def truncPrimes(amount):
    st = T.time()
    sum = 0
    found = 0
    checkNum = 10
    while found < amount:
        if checkLeftTruncNum(checkNum) and checkRightTruncNum(checkNum):
            sum += checkNum
            found += 1
            checkNum += 1
        else:
            checkNum += 1
    tt = T.time() - st
    print "The sum of", amount, "truncatable primes is:", sum
    print "This program took", tt, "seconds to run"


if __name__ == "__main__":
    import sys
    truncPrimes(int(sys.argv[1]))

