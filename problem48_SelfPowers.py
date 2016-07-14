# Euler Problem 48:
# The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.
# Find the last ten digits of the series, 1^1+2^2+3^3+...+ 1000^1000.

# Solution:
#----------------------------------------------------------
# Well there's clearly the brute force way to do this. That would
# require summing up to a number bigger than 1000^1000 which is
# 3*1000=3000 digits and ~1000 clock cycles (probably less! but that's a little
# to technical to go into here). This is doable with the computers we have
# today operating on the scale of gigahertz. A (perhaps) more
# efficient solution would be to mod 10000000000 each n^n as it was
# calculated then add that to the sum. This will result in only adding numbers
# with 10 digits onto the running sum. Lastly we can quickly check if mod-ing
# that resulting sum at each step would speed things up as well (I highly
# doubt it, adding 1000 10 digit numbers together isn't that bad).

# Confirmed, without modding at each step is pretty much exactly as fast as
# with modding at each step (therefore modding the sum would be the same as
# well).


import time as T


def lastTenDigs(n):
    st = T.time()
    sum = 0
    for i in range(1, n+1):
        sum += i**i
    ans = sum % 10000000000
    tt = T.time() - st
    print "The last 10 digits of sum(", n, "^", n, ") is:", ans
    print "lastTenDigs function ran in:", tt, "seconds"

def lastTenDigsWithModPowers(n):
    st = T.time()
    sum = 0
    for i in range(1, n+1):
        sum += i**i % 10000000000
    ans = sum % 10000000000
    tt = T.time() - st
    print "The last 10 digits of sum(", n, "^", n, ") is:", ans
    print "lastTenDigsWithModPowers function ran in:", tt, "seconds"

if __name__ == "__main__":
    import sys
    lastTenDigs(int(sys.argv[1]))
    lastTenDigsWithModPowers(int(sys.argv[1]))
