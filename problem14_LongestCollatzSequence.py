# Euler Problem 14:
# The following iterative sequence is defined for the set of positive integers:
#       n -> n/2 (n is even)
#       n -> 3n +1 (n is odd)
# Using the rule above and starting with 13, we generate the following
# sequence:
#       13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
# It can be seen that this sequence (starting at 13 and finishing at 1)
# contains 10 terms. Although it has not been proved yet (Collatz Problem), it
# is thought that all starting numbers finish at 1.

# Which starting number, under one million, produces the longest chain?
# NOTE: Once the chain starts the terms are allowed to go above one million.

import time as T

def lengthCS(num, count=1):
    if num == 1:
        return count
    elif num % 2 == 1:
        count += 1
        return lengthCS(3*num+1,count)
    else:
        count += 1
        return lengthCS(num/2, count)


def longestCSUnder(n):
    start_time = T.time()
    maxLen = 1
    maxNum = 1
    for num in range(1,n+1):
        numLen = lengthCS(num)
        if numLen > maxLen:
            maxLen = numLen
            maxNum = num    #optional but just out of curiosity
    total_time = T.time()-start_time
    print "The number", maxNum, "has the longest Collatz sequence under", n, "with", maxLen, "terms"
    print "This program took", total_time, "seconds to run"

# Note that the above function (in particular the recursive lengthCS function)
# in many cases we will hit a number in the sequences where we've already
# determined how long the chain from that point will be. Therefore if we simply
# create a hashtable (dictionary (global?)) every time we calculate a CS length
# and store our values in there (and look them up as need be), we should
# optimize this search
#
# TODO: work on this, need to memoize somehow



def dictLongestCS(n, csDict = {1:1}):
    if not n in csDict:
        if n % 2 == 1:
            csDict[n] = dictLongestCS(3*n+1)+1
        else:
            csDict[n] = dictLongestCS(n/2)+1
    return csDict

def longestCSUnder2(n):
    for num in range (1,n+1):
        dictLongestCS(num)
    print csDict.keys()[csDict.values().index(max(csDict.values()))]

if __name__ == "__main__":
    import sys
    longestCSUnder(int(sys.argv[1]))



