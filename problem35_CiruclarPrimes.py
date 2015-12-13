# Euler Problem 35
# The number, 197, is called a circular prime because all rotations of the
# digits: 197, 971, and 719, are themselves prime.
#
# There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71,
# 73, 79, and 97.
#
# How many circular primes are there below one million?

import time as T

def rotate(num):
    # note that a number with a zero as the second (and continuing) digit will
    # end up being a smaller length, ie rotate(1001) -> 11
    strNum = str(num)
    firstChar=strNum[0]
    strNum = strNum + firstChar
    strNum = strNum[1:]
    ans = int(strNum)
    return ans

def isPrime(num): # Fast primality test using a 2 3 wheel
    if num<2: return False
    if num==2: return True
    if num==3: return True
    if num%2==0: return False
    if num%3==0: return False
    i=5
    w=2
    while i*i <= num:
        if num%i==0:
            return False
        i += w
        w =6-w
    return True

def circulate(num): # returns a list of the canonical rotations of the number using rotate function
    turns = len(str(num))-1
    lst = [num]
    for _ in range(turns):
        num = rotate(num)
        lst.append(num)
    return lst

def checkLst(lst):
    for i in lst:
        if not isPrime(i):
            return False
    return True

def circPrime(limit):
    st = T.time()
    count = 2 # 2 and 5 are the first two circular prime and I'd rather not check numbers with a 2 or 5 in it as we know they can't be circular primes (note could also optimize by checking if there exists an even digit
    for num in range(1,limit):
        strRep = str(num)
        if "0" not in strRep and "2" not in strRep and "5" not in strRep:
            if checkLst(circulate(num)):
                count += 1
    tt = T.time()-st
    print "There are", count, "Circular Primes below", limit
    print "This program took", tt, "seconds to run"




if __name__== "__main__":
    import sys
    circPrime(int(sys.argv[1]))
