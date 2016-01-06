# Euler Problem 38:
# Take the number 192 and multiply it by each of 1, 2, and 3:
#       192 x 1 = 192
#       192 x 2 = 384
#       192 x 3 = 576
#
# By concatenating each product we get the 1 to 9 pandigital,
# 192384576. We will call 192384576 the concatenated product of 192 ans
# (1,2,3)
#
# The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4,
# and 5, giving the pandigital, 918273645, which is the concatenated product
# of 9 and (1,2,3,4,5).
#
# What is the largest 1 to 9 pandigital 9-digit number that can be formed
# as the concatenated product of an integer with (1,2,...,n) where n>1?

# Solution:
# Since we must go up to at least n=2 we need to have the
# concatenation of two numbers with at least one less than five digits in
# length. A rough upper bound for this is 10000 since concatenating 1*10000
# and 2*10000 gives a 10 digit number which can't satisfy our
# pandigital criteria, further more any multiplier higher will also produce
# >= 10 digits when concatenating the first two terms.
# We can now loop 1:10000 checking the set (1,...,n) for pandigitals until we
# reach a 10 digit number (no pandigitals beyond 10 digits)


import time as T

def isPandigital(n):
    digs = ['1','2','3','4','5','6','7','8','9']
    strRep = str(n)
    if strRep.count('0') > 0:
        return False
    for i in digs:
        if strRep.count(i) != 1:
            return False
    return True



def main(inp):
    print "isPandigital Test:", isPandigital(inp)


if __name__ == "__main__":
    import sys
    main(int(sys.argv[1]))
