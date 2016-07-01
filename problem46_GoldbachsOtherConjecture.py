# Euler Problem 46:
# It was proposed by Christian Goldbach that every odd composite number can be
# written as the sum of a prime and twice a square.
#           9 = 7 + 2x1^2
#           15 = 7 + 2x2^2
#           21 = 3 + 2x3^2
#           25 = 7 + 2x3^2
#           27 = 19 + 2x2^2
#           33 = 31 + 2x1^2
# It turns out that the conjecture was false.
#
# What is the smallest odd composite that cannot be written as the sum of a
# prime and twice a square?

# Solution:
#----------------------------------------------------------
# Starting at 33, generate the next odd number (fairly simple), check the
# length of the prime decomposition, if it's greater than 1 it's not a prime
# and is therefore a composite and a candidate for the answer. Next we have an
# option of either generating the list of primes under that number and checking
# if the (number - each prime)/2 is a square, or generating all the squares
# under that number, then checking if the number - each square*2 is a prime.
# Whichever method we choose, if we exhaust the list and find no solutions that
# form the number with a prime + twice a square then we've found the smallest
# odd composite that disproves the conjecture. I'm going to choose to
# generating the squares under that number because this grows faster (less
# combinations to check) than generating all the primes under a number, plus
# the primality check is pretty quick as well.

import time as T

def main():
    st = T.time()
    check = 35
    found = False

    while not found:
        if len(primeFactors(check)) > 1:
            lst = lstSquaresX2(check)
            lstCheck =[]
            for expX2 in lst:
                lstCheck.append(isPrime(check-expX2))
            if True not in lstCheck:
                found = True
                ans = check
        check += 2
        tt = T.time()-st
    print "The first odd composite number that cannot be written as the sum of a prime and twice a square is:", ans
    print "This program took", tt, "Seconds to run"



def primeFactors(num):
    primeDecomp = []
    i = 2
    while i <= num:
        while num%i == 0:
            primeDecomp.append(i)
            num /= i
        i += 1
    return primeDecomp

def lstSquaresX2(num):
    curr = 2
    lst = [2]

    while curr**2*2<num:
        lst.append(curr**2*2)
        curr+=1
    return lst

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


if __name__ == "__main__":
    main()


