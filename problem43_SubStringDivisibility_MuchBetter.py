# Euler Problem 43:
# The number, 1406357289, is a 0 to 9 pandigital number because it is made up
# of each of the digits 0 to 9 in some order, but it also has a rather
# interesting sub-string divisibility property.
#
# Let d_1 be the first digit, d_2 be the second digit, and so on. In this way,
# we note the following:
#
# d_2d_3d_4=406 is divisible by 2
# d_3d_4d_5=063 is divisible by 3
# d_4d_5d_6=635 is divisible by 5
# d_5d_6d_7=357 is divisible by 7
# d_6d_7d_8=572 is divisible by 11
# d_7d_8d_9=728 is divisible by 13
# d_8d_9d_10=289 is divisible by 17
#
# Find the sum of all 0 to 9 pandigital numbers with this property.

import time as T

st = T.time()

def converter(z):
    if len(z) == 2:
        return '0'+z
    elif len(z) == 1:
        return '00'+z
    return z


def m(n):
    """function to generate multiples
    of given number under 1000"""
    mn = []
    mul = 1
    i = 1
    while mul < 1000:
        mul = i*n
        i += 1
        mn.append(mul)
    mn.pop()
    mn = map(str, mn)
    mn = map(converter, mn)
    return mn


def concat(a, b):
    """function to form the solution"""
    c = []
    for i in a:
        for j in b:
            if i[:2] == j[1:] and len(set(j[0] + i)) == len(j[0] + i):
                c.append(j[0] + i)
    return c


def missing(g):
    """function to add the missing number from
    0-9 to complete the pandigital number"""
    for i in '0123456789':
        if i not in g:
            return i + g

# forming the multiples of 2,3,5,7,11,13
m17, m13, m11, m7, m5, m3, m2 = (m(17), m(13), m(11), m(7), m(5), m(3), m(2))

# getting the required solution
d = reduce(concat, [m17, m13, m11, m7, m5, m3, m2])

# adding the missing number
d = map(missing, d)

# converting the numbers to int
d = map(int, d)

ans = sum(d)

tt = T.time()-st

print "The sum of all 0-9 pandigitals with the specificed prime divisibility criteria of its length 3 substrings is:", ans
print "This program took", tt, "seconds to run"
