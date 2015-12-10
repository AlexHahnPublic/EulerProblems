# Euler Problem 28:
# Starting with the number 1 and moving to the right in a clockwise direction a
# 5 by 5 spiral is formed as follows:

#           21 22 23 24 25
#           20  7  8  9 10
#           19  6  1  2 11
#           18  5  4  3 12
#           17 16 15 14 13

# It can be verified that the sum of the numbers on the diagonals is 101.

# What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral
# formed in the same way?

# Solution
# -------------------------------------------------------------------

# So there's an actual underlying physical methodology to generate the next
# diagonal number to add to the running sum. Because this follows a very
# physical underlying methodology there's a very strong chance that there's a
# closed form function about how this sum grows. Let's write out the series for
# the sum of the first few n x n spirals then used some methodology (think
# divided difference) to find the closed form solution

# n = 3
#
#           7 8 9
#           6 1 2
#           5 4 3
#
# S(3)= 25

# n = 5
#
#          21 22 23 24 25
#          20  7  8  9 10
#          19  6  1  2 11
#          18  5  4  3 12
#          17 16 15 14 13
#
# S(5) = 101

# n = 7
#
#        43 44 45 46 47 48 49
#        42 21 22 23 24 25 26
#        41 20  7  8  9 10 27
#        40 19  6  1  2 11 28
#        39 18  5  4  3 12 29
#        38 17 16 15 14 13 30
#        37 36 35 34 33 32 31
#
# S(7) = 261

# n = 9
#
#     73 74 75 76 77 78 79 80 81
#     72 43 44 45 46 47 48 49 50
#     71 42 21 22 23 24 25 26 51
#     70 41 20  7  8  9 10 27 52
#     69 40 19  6  1  2 11 28 53
#     68 39 18  5  4  3 12 29 54
#     67 38 17 16 15 14 13 30 55
#     66 37 36 35 34 33 32 31 56
#     65 64 63 62 61 60 59 58 57
#
# S(9) = 537

# We (hopefully) have solved for enough data points to use the divided
# difference method to interpolate this closed form equation. Here's what our
# divided difference pyramid (or whatever you want to call it looks like):


#    tier 3          32  | 32
#    tier 2       52  | 84  |  116
#    tier 1    24  |  76 | 160 | 276
#    y_i's   1  |  25 | 101 | 261 | 537
#    -----------------------------------
#    x_i's   1  |  3  |  5  |  7  |  9


# It's no coincidence that the third tier seems to be constant (and if we
# solved for another s, say S(11), we'd see that this row would always be 32's
# across). This tells us the order of the polynomial!

# We're looking for something of the form S(n)= An^3+ Bn^2 + Cn + D


# When n=1 we have:
#   A + B + C + D = 1

# When n=3 we have:
#   27A + 9B + 3C + D = 25

# When n=5 we have:
#   125A + 25B + 5C + D = 101

# When n=7 we have:
#   343A + 49B + 7C + D = 261

# When n=9 we have:
#   729A + 81B + 9C + D = 537


# At this point we have four equations and four unknowns so we can solve
# accordingly. Note that I only fleshed out the n=9 case so I could show that
# the third divided difference would always be constant indicating a third
# degree polynomial. Also note that I only used the odd's case because I wasn't
# sure that the fact that we explicitly didn't double count the middle entry in
# the odd array but wouldn't run into that problem with the evens case. We'll
# check after solving this equation!

# The augmented array looks like:
#
# [   1    1    1   1   1
#     27   9    3   1   25
#     125  25   5   1   101
#     343  49   7   1   261 ]

# We could solve this by hand Using Gaussian elimination then back substitution
# or with matrix inversion but... we have computers
#
# Entering in python:
#
# >>> import numpy as np
# >>> A = np.array([[1,1,1,1], [27,9,3,1], [125,25,5,1], [343,49,7,1]])
# >>> b = np.array([1,25,101,261])
# >>> x = np.linalg.solve(A,b)

# We get something like x = [0.666667, 0.5, 1.33333, -1.5]
#
# From here it's clear that our coefficients are A=2/3, B=1/2, C=4/3, and
# D=-3/2

def NumSpiralDiags(n):
    import time as t
    start_time = t.time()
#DON'T USE INT HERE! THROWS ANSWER OFF BY 1!!! very interesting
    ans = (2.0/3.0)*(n**3.0)+(1.0/2.0)*(n**2)+(4.0/3.0)*(n)-(3.0/2.0)
    total_time = t.time() - start_time
    print "The sum of the diagonals of a consecutive integer spiral forming an", n, "x", n, "array is:", ans
    print "This program took", total_time, "seconds to run"

if __name__ == "__main__":
    import sys
    NumSpiralDiags(int(sys.argv[1]))




