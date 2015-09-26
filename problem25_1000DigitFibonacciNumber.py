# Euler Problem 25:
# The Fibonacci sequence is defined by the recurrence relation:
#       F_n = F_{n-1} + F_{n-2},
# where,
#       F_1=1 and F_2=1
# Hence the first 12 terms will be:
#   F_1 = 1
#   F_2 = 1
#   F_3 = 2
#   F_4 = 3
#   F_5 = 5
#   F_6 = 8
#   F_7 = 13
#   F_8 = 21
#   F_9 = 34
#   F_10 = 55
#   F_11 = 89
#   F_12 = 144
# The 12th term,F_12 is the first term to contain three digits.
# What is the first term in the Fibonacci sequence to contain 1000 digits?

import time

def FibSumNumDigs(digs):
    counter=2
    F_prev = 1
    F_curr = 1
    while len(str(F_curr)) < digs:
        F_temp=F_prev
        F_prev=F_curr
        F_curr += F_temp
        counter += 1
    print counter

if __name__ == "__main__":
    import sys
    FibSumNumDigs(int(sys.argv[1]))
