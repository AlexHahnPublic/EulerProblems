# Euler Problem 52:
# It can be seen that the number, 125874, and its double, 251748, contain
# exactly the same digits but in a different order.
#
# Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x,
# contain the same digits.

# Solution:
# ---------------------------------------------------------
# I believe that a brute force analysis would suffice for this type of problem
# although there are some basic restrictions that could limit the search space
# greatly. Ie since we know the multiples must contain the same exact digits
# (the same number of times) we know that we can't cross over an order of
# magnitude when multiplying by 6. So say we're in the thousands, we know that
# we only have to check up to roughly floor(9999/6)= 1666 because any number
# higher than that will have 6x > 10000 and therefore can't contain the exact
# same digits. This would reduce our search space by about a factor of 10. We
# can code it in later if our runtime is a little too high.
#
# The brute force algorithm will basically:
#   1) Start with a number and call a function to create a dictionary of its
#   digit - count pairs (or just use a list which increases that digits index
#   for each digit count)
#   2) Multiply the number by 2, 3, 4, 5, and 6.
#   3) Call the count digits function again on the 5 new numbers.
#   4) Check if all lists are equal, if so, then the first to do this is the
#   answer

import time as T


def main(numMults):
    st =  T.time()
    found = False
    check = 1 # Note could very logically argue that this should start a bit
              # higher but this only waists maybe a couple clock cycles...

    while not found:
        chkList = countDigs(check)
        cont = True
        mult = 2
        while cont and mult <= numMults:
            againstList = countDigs(mult*check)
            if chkList != againstList:
                cont = False
            else:
                mult += 1
        if cont == True:
            ans = check
            found = True
        else:
            check += 1
    tt = T.time() - st
    print "The first number whose 1 through", numMults, "multiples contain the same exact digits (up to duplicity as well) is:", ans
    print "This program took", tt, "seconds to run"


def countDigs(num):
    strNum = str(num)
    digList = [0]*10
    for c in strNum:
        digList[int(c)] += 1
    return digList


if __name__ == "__main__":
    import sys
    main(int(sys.argv[1]))





