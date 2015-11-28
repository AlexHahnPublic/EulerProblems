# Euler Problem 31:
# In England the currency is made up of pound, L, and pence, p, and their are
# eight coins in general circulation:

#       1p, 29, 5p, 10p, 20p, 50p, 1L (100p), and 2L (200p)

# It is possible to make 2L in the following way:

#       1x1L + 1x 50p + 2x20p + 1x5p + 1x2p + 3x1p

# How many different ways can 2L be made using any number of coins?

# Solution
# -----------------------------------------------

# There are generally two ways to go about this problem; one much more eloquent
# than the other.

# Basic strategy:
# Iterate through all the combinations via nested for loops in decreasing
# order, ie 100s, 50s, 20s, etc, adding smaller coins bounded by some upper
# bound until sum 200p is met (increment number of ways variable)

# Much more eloquent algorithm:
# This is a classical problem in dynamic programming who's basic tenant is
# break the larger problem at hand into smaller sub problems and solve those.
# For example this is tantamount to saying once we know all the ways to make
# 20p (one 20p coin combination) we no longer have to do any calculations
# involving any combinations to make 20p since we already know how (obviously
# need to memoize as we go). Basically for each coin denomination i we can
# compute the combination of ways to create that amount using the next smallest
# unit. Since we build up we can continue to use the combinations of the
# smaller amounts we've already calculated^^

def coinSums(n):
    denoms=[1, 2, 5, 10, 20, 50, 100, 200] #different denominated amounts
    combs=[1]+[0]*n # list of combinations to make each denomination
    for pence in denoms:
        for i in range(pence,n+1):
            combs[i] += combs[i-pence]
    print "The number of different combinations to make", n, "pence is:", combs[n]

if __name__=="__main__":
    import sys
    coinSums(int(sys.argv[1]))


