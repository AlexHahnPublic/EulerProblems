# Euler Problem 7:
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see
# that the 6th prime number is 13.

# What is the 10001st prime number?

#Solution, Off the top of my head we could either greedily use trial division
# or more efficiently use a Sieve (Sieve of Eratosthenes)

# Using the contrapositive of if a number n is composite then it has at leas
# one divisor less than sqrt(n)

import time

def isPrime(num):
    i = 2
    boolVal = True
    while i*i <= num and boolVal == True:
        if num%i == 0:
            boolVal = False
        else:
            i += 1
    return boolVal




#Trial Division ignoring even numbers
def findNthPrime(n):
    start_time = time.time()
    num2check = 3
    counter = 1
    while counter < n:
        if isPrime(num2check) and counter != n-1:
            counter += 1
            num2check += 2 # evens can't be prime
        elif isPrime(num2check) and counter == n-1:
            break
        else:
            num2check +=2
    total_time = time.time() - start_time
    print "The", n, "prime number is:", num2check
    print "This program took:", total_time, "seconds to run"



#def findNthPrime(n):
#    currNum = 2
#    nums = range(1,n+1)
#    while len nums > 1 and currNum < n
#        multiplier =

if __name__ == "__main__":
    import sys
    findNthPrime(int(sys.argv[1]))
