# Euler Problem 16:
# 2^15 = 32768 and the sum of its digits is
#       3 + 2 + 7 + 6 + 8 = 26
# What is the sum of the digits of the number 2^1000?

import time as T

def sumDig(n):
    start_time = T.time()
    inp = 2**1000
    total = 0
    strRep = str(long(inp))
    for dig in strRep:
        total += int(dig)
    total_time = T.time()-start_time
    print "The sum of the digits in the number 2^1000 is:", total
    print "This program took", total_time, "seconds to run"


if __name__ == "__main__":
    import sys
    sumDig(int(sys.argv[1]))

# One Liner: (haven't verified)
#print sum(int(digit) for digit in str(2^1000))

# One liner using a lambda (anonymous function)
#reduce(lambda x, y: x+y, [int(i) for i in str(2**1000)])

