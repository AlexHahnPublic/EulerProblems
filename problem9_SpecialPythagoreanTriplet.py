# Euler Problem 9:
# A Pythagorean triplet is a set of three natural numbers, a < b < c, for
# which,
#           a^2 + b^2 = c^2
# For example 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc

import time

# Brute force but using the fact that a+b+c=1000 => c=1000-a-b

def pythags(n):
    start_time = time.time()
    for a in range(1,(n+1)/2):
        for b in range(1,(n+1)/2):
            if a**2+b**2 == (n-a-b)**2:
                print "a, b, and c are:", a, b , n-a-b
                print "They multiply to:", a*b*(n-a-b)
    total_time = time.time() - start_time
    print "This program took:", total_time, "seconds to run"

# Using a little more mathematical simplifications
#       a+b+c=1000
# Square both sides:
#       a^2+b^2+c^2+2(ab+bc+ac)=10^6
# We can rewrite c^2 as a^2+b^2 since this a Pythagorean triple:
#       2(a^2+b^2)+2(ab+bc+ac)=1000
# Divide through by 2:
#       a^2+b^2+ab+bc+ac=500
# Add ab to each side (to complete the square):
#       a^2+b^2+2ab+bc+ac=500+ab
# Rewrite as the square:
#       (a+b)^2+bc+ac=500+ab
# Factor out the c where appropriate:
#       (a+b)^2+c(a+b)=500+ab
# Factor out the (a+b):
#       (a+b)(a+b+c)=500+ab:
# Using a+b+c=1000 and distributing:
#       1000a+1000b=500+ab
# Finally:
# 1000a+1000b-ab=500:
#
# So simply solve for a nd b s.t. the above equation holds
#
# This still involves a double for loop so it would take about as much time as
# the above solution. Working on a much more elegant solution

#TODO: not Correct yet but close!
def pythags2(n):
    for i in range(1,(n+1)/2):
        for j in range(1,(n+1)/2):
            if 1000*i + 1000*j - i*j == 500:
                print "a, b, and c are:", i, j, n-i-j
                print "They multiply to:", i*j*(n-i-j)





if __name__ == "__main__":
    import sys
    pythags(int(sys.argv[1]))



