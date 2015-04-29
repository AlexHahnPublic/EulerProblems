# Euler Problem 1:
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we # get 3, 5, 6, and 9. The sum of these multiples is 23

# SOLUTION

# Find the sum of all the multiples of 3 and 5 below 1000.
#
# Note that for any arithmetic with initial term a_1 and common difference
# between consecutive terms d we can write the nth term as:
#           a_n = a_1 + (n - 1)d        (1)
# and in general
#           a_n = a_m + (n - m)d        (2)

# To derive a formula for the sum of a finite arithmetic sequence let's write
# out the sum in two fairly straight forward ways:
#       S_n = a_1 + (a_1+d) + (a_1+2d) + ... + (a_1+(n-2)d) + (a_1+(n-1)d)  (3)
#       S_n = (a_n-(n-1)d) + (a_n-(n-2)d) + ... + (a_n-2d) + (a_n-d) +a_n   (4)

# Adding together both sides of the two equations all the terms involving d
# cancel on the RHS leaving us with n a_1's and n a_n's
#       2S_n = (na_1+na_n)      (5)
#    => S_n  = n(a_1+a_n)/2     (6)

# Now we can write out the sums of the two sequences in the problem:

# First note that there are floor(Number to stay under/d) terms for whatever
# arithmetic series we're taking, in this case 1000, so for the d=3 series
# there are floor(1000/3)=333 terms and in general since
# a_1+(n-1)d=x (last term, must be under bounding number) we can safely say
# that the number of terms is
#       n = floor(((x-a)/d)+1)      (7)

# Since in this problem a_1 = d itself (the first term is the distance from
# zero to a_1 which is d) we can rewrite the formula as:
#       n = floor(((x-d)/d)+1)      (8)
#    => n = floor((x/d)-1+1)        (9)
#    => n = floor(x/d)              (10)
#    (which as noted above for the example of 1000 and d=3 lines up)

# Therefore we can now calculate the general form of the last term (so we can
# use equation (6) above)
#       a_n = a_1 + (n-1)d
#       =>  = d + (floor(x/d)-1)d
#       =>  = d(floor(x/d))
#       (which also makes perfect sense, the distance multiplied by the number
#       of times you can whole-ly fit it under the bounding number)

# So now we can write the sum as:
#       S_n  = n(a_1+a_n)/2
#       =>   = floor(x/d)(d+d(floor(x/d)))/2

# We are almost done, but first we must notice that if we add the sum of the
# sequences for d=3 and d=5 together we'll be double counting (the first common
# number is 15).
# To deal with this we can simply note that the least common multiple of 3 and
# 5 is 15 (since 3 and 5 are co-prime lcm(3,5)=3*5), and get rid of all the
# multiples of 15, which is itself a proper arithmetic sequence
#
# We get (n=under 1000 => n=999):
#       Total = S_3(n=floor(x/d)) + S_5(n=floor(x/d)) - S_15(n=floor(x/d))
#       Total = floor(999/3)(3+3(floor(999/3)))/2
#               + floor(999/5)(5+5(floor(999/5)))/2
#               - floor(999/15)(15+15(floor(15/15)))/2
#
# instead of writing out a hardcoded equation let's write a function that takes
# in a number to stay under, in this case 999 and returns the sum of all
# numbers divisible by just 3 or 5
import math
import time

def sumArithmeticSeries(numStayUnder,d):    # assuming starting at 0
                                            # so d = a_1
    start_time = time.time()
    seriesSum = math.floor(numStayUnder/d)*(d+d*math.floor(numStayUnder/d))/2
    return seriesSum

def sum3and5(n):
    start_time = time.time()
    numStayUnder = n-1
    total = sumArithmeticSeries(numStayUnder,3) + sumArithmeticSeries(numStayUnder,5) - sumArithmeticSeries(numStayUnder,15)
    total_time = time.time() - start_time
    print "The sum of all the multiples of 3 and 5 below", n, "is", total
    print "This program took:", total_time, "seconds to run"

if __name__ == "__main__":
    import sys
    sum3and5(int(sys.argv[1]))
