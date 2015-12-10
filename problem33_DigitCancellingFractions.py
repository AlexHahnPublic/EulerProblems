# Euler Problem 33:
# The fraction 49/98 is a curious fraction, as an inexperienced mathematician
# in attempting to simplify it may incorrectly believe that 49/98=4/8, which is
# correct, is obtained by cancelling the 9s.
#
# We shall consider fractions like, 30/50=3/5, to be trivial examples.
#
# There are exactly four non-trivial examples of this type of fraction, less
# than one in value, and containing two digits in the numerator and
# denominator.
#
# If the product of these four fractions is given in its lowest common terms,
# find the value of the denominator.


import time as T
import fractions as F

def digCancelFracs():
    st = T.time()
    mult = 1
    nums = []
    denoms = []
    for denominator in range(11,100):
        for numerator in range(11,denominator):
            tup=cancellation(numerator,denominator)
            if denominator%10 != 0 and tup != "not a candidate" : # make sure not a "trivial" case and an actual cancellation occurs
                val=float(numerator)/denominator
                if checkEquality(val, tup):
                    nums.append(tup[0])
                    denoms.append(tup[1])
    top = reduce(lambda x, y: int(x)*int(y), nums)
    bottom = reduce(lambda x, y: int(x)*int(y), denoms)
    ans= F.Fraction(float(top)/float(bottom)).limit_denominator()
    tt = T.time() - st
    print "The reduced multiplication of all fractions with two nonzero digits in the numerator and denominator that can be solved validly via cancellation is", ans
    print "This program took", tt, "seconds to run"




def cancellation(numerator, denominator):
    strNum = str(numerator)
    strDen = str(denominator)
    for i in strDen:
        if i in strNum:
            strNum = strNum.replace(i, '', 1)
            strDen = strDen.replace(i, '', 1)
    if len(strNum) == 1:
        return (strNum, strDen)
    else:
        return "not a candidate"

def checkEquality (val, tup):
    if val == float(tup[0])/float(tup[1]):

        return True
    else:
        return False




if __name__ == "__main__":
    digCancelFracs()


