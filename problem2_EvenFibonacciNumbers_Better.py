# Euler Problem 2:
# Each new term in the Fibonacci sequence is generated by adding the previous
# two terms. By starting with 1 and 2, the first 10 terms will be:
#       1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
# By considering the terms in the Fibonacci sequence whose values do not
# exceed four million, find the sum of the even-valued terms

# In this more efficient solution we calculate only each consecutive even
# Fibonacci term and add it to the total. This eliminates two thirds of all of
# the numbers if we just calculated all of the Fibonacci numbers and checked if
# they were divisible by 2 or not then add

# SOLUTION
# We can find the relative distance between Fibonacci numbers! This is simply
# the golden ratio in the limit, lim f_n/f_{n-1} as n tends towards infinity.
# since we know the relative distance between consecutive terms and we know
# that all of the even terms are once every three terms (odd+even=even,
# even+odd=odd, odd+odd=even...) we can always calculate the next even fibonacci
# term (roughly, the golden ratio is an irrational and so therefore is phi^3,
# we can just take enough precision and round!) and add it to a running total.

import time

def sumEvenFibs(under):
    start_time = time.time()
    phi = 1.6180339887498948482045868343656381177203091798057628
    dist3terms = phi**3
    currEvenFib = 2
    total = 0
    while currEvenFib < under:
        total += currEvenFib
        currEvenFib = round(currEvenFib*dist3terms)
    total_time = time.time() - start_time
    print "The sum of all the Fibonacci numbers that do not exceed", under, "is:", int(total)
    print "This program took:", total_time, "seconds to run"

if __name__ == "__main__":
    import sys
    sumEvenFibs(int(sys.argv[1]))
