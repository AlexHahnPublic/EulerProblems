# Euler Problem 3:
# The prime factors of 13195 are, 5, 7, 13, and 29
# What is the largest prime factor of the number 600851475143?

def largestPrimeFactor(n):
    original_n = n
    i = 2
   # This nex statement is often confused/ not stated correctly as "the largest
   # prime factor of a (composite) number is less than sqrt(n)". That's simply
   # not true, take a look at 14=7*2 and sqrt(14)=3 something. Really the
   # statement is: for every composite number n there exists a prime p s.t.
   # p<sqrt(n). We can still leverage this fact! Many people just claim so for
   # the wrong reason. Basically we only need to check up to the sqrt(n)
   # integer divisors to tell whether the number n is prime or not (obviously can't be
   # prime if a number < sqrt(n) divides it, but more importantly must be prime
   # if no integers< sqrt(n) divide it). TODO: Prove it^^
   # Also TODO: this doesn't really work for numbers = prime^x (x an integer)
   # because it will always satisfy n % i == 0, becomes rare the larger the
   # number is but still, need to add in some sort of condition or subfunction.
   # Actually upon further thought this won't work whenever the largest prime
   # has multiplicity greater than 1... really need to fix! The only thing I
   # can think of off the top of my head is to check the bool of a subfunction
   # that checks whether the modulo is an integer root of the number, if true
   # then just exit the loop, if false continue into the inner loop
    while i * i <= n:
        print "inner loop, i is currently: ", i
        while n%i == 0:
            print n,"(mod ", i, ")=0"
            n /= i
            print "So divide n by ", i, "so n= ",n
        i = i + 1 # Someone once told me increment this by 2 coz "it's faster
                  # in larger n", this can only be done after 2 and 3 is 
                  #completely factored out.. not sure worth the code change
        print "outside inner loop, increment i, i is now: ", i
    print n

if __name__ == "__main__":
    import sys
    largestPrimeFactor(int(sys.argv[1]))

