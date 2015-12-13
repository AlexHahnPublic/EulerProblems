# Euler Problem 35:
# The decimal number, 585 = 1001001001_2 (binary), is palindromic in both
# bases.
# Find the sum of all numbers, less than one million, which are palindromic in
# base 10 and base 2.
# (Please note that the palindromic number, in either base, may not include
# leading zeros.)


import time as T


def convert10_2(num):
    if num == 0:
        return ""
    else:
        return convert10_2(num/2) + str(num%2)

def checkIsPal(string):
    if len(string) <= 1:
        return True
    elif string[0] == string[len(string)-1]:
        return checkIsPal(string[1:len(string)-1])
    else:
        return False


def dubBasePals(n):
    st = T.time()
    total = 0
    for num in range(1,n):
        if checkIsPal(str(num)) and checkIsPal(str(convert10_2(num))):
            total += num
    tt = T.time()-st
    print "The sum of all palindromic numbers in both base 10 and base 2 under", n, "is:", total
    print "This program took", tt, "seconds to run"


if __name__ == "__main__":
    import sys
    dubBasePals(int(sys.argv[1]))



