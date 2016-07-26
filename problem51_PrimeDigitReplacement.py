# Euler Problem 51:
# By replacing the 1st digit of the 2-digit number *3, it turns out that six of
# the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.
#
# By replacing the 3rd and 4th digits of 56**3 with the same digit, this
# 5-digit number is the first example having seven primes among the ten
# generated numbers, yielding the family: 56003, 56113, 56333, 56443, 56663,
# 56773, 56993. Consequently 56003 being the first member of this family, is
# the the smallest prime with this property.
#
# Find the smallest prime which, by replacing part of the number (not
# necessarily adjacent digits) with the same digit, is part of an eight prime
# value family.

# Solution:
# ---------------------------------------------------------
# Right off the bat we know that permuting the last digit (with any combination
# of other digits) will not possibly provide an answer since half of those
# candadites will be even and therefore could not be prime, leaving at most 5
# primes in the family. This means we will only have to permute the first n-1
# digits in all the combinations.
# I think that the best algorithmic approach to this problem would be to:
#   1) generate the first n primes (say 100)
#   2) starting with the first digit, cycle though the digits, while checking
#   primality at each rotation of the digit. Note to keep track of how many are
#   not prime. Once you find 3 that are not prime you can stop the rotation as
#   their will not be a way to end up with 8 of the 10 cycled numbers being
#   prime.
#   3) Move to the second digit and repeat step 2. Continue in this manner
#   until
