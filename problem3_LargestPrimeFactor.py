# Euler Problem 3:
# The prime factors of 13195 are, 5, 7, 13, and 29
# What is the largest prime factor of the number 600851475143?
import time

def largestPrimeFactor(n):
    start_time = time.time()
    original_n = n
    i = 2
   # This nex statement is often confused/ not stated correctly as "the largest
   # prime factor of a (composite) number is less than sqrt(n)". That's simply
   # not true, take a look at 14=7*2 and sqrt(14)=3 something. Really the
   # statement is: for every composite number there exists a prime p s.t.
   # p<sqrt(n). We can still leverage this fact! Many people just claim so for
   # the wrong reason. Basically we only need to check up to the sqrt(n)
   # integer divisors to tell whether the number n is prime or not (obviously can't be
   # prime if a number < sqrt(n) divides it, but more importantly must be prime
   # if no integers< sqrt(n) divide it). TODO: Prove it^^
    while i * i <= n:
        while n%i == 0:
            n /= i
        i = i + 1 # TODO: Someone once told me increment this by 2 coz "it's faster,
                  #not sure about that, need to check, kinda makes sense
    total_time = time.time() - start_time
    print "The largest prime factor of the number", original_n, "is", n
    print "This program took:", total_time, "seconds to run"

if __name__ == "__main__":
    import sys
    largestPrimeFactor(int(sys.argv[1]))

