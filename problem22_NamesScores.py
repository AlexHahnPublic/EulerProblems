# Euler Problem 22:
# Using names.txt, a 46K (kilobyte) text file containing over five-thousand
# first names, begin by sorting it into alphabetical order. Then working out
# the alphabetical value for each name, multiply this by its alphabetical
# position in the list to obtain the score.

# For example, when the list is sorted into alphabetical order, COLIN, which is
# worth 3+15+12+9+14=53, is the 938th name in the list. So, COLIN would obtain
# a score of 938x53=49714.

# What is the total of all the name scores in the file?

import time as T

def nameScore(filename):
    index = 1
    start_time=T.time()
    total = 0
    scores={
            'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8,'I':9,'J':10,'K':11
            ,'L':12,'M':13,'N':14,'O':15,'P':16,'Q':17,'R':18,'S':19,'T':20,'U'
            :21,'V':22,'W':23,'X':24,'Y':25,'Z':26, '"':0}
    srtLst=getSortedList(filename)
    for name in srtLst:
        nameTotal=0
        name=name.rstrip('\n')
        for letter in name:
            nameTotal += scores[letter]
        total += index*nameTotal
        index += 1
    total_time=T.time()-start_time
    print "The name score sum of the file", filename, "is", total
    print "With Alex's method this program took", total_time, "seconds to run"

def getSortedList(filename):
    for line in open(filename):
        unsrtLst = line.split(',')
        #srtLst = sorted(unsrtLst) # Using built in list sort function
    return quickSort(unsrtLst)

def quickSort(lst):
    if not lst:
        return []
    return (quickSort([x for x in lst[1:] if x<lst[0]])
            + [lst[0]] +
            quickSort([x for x in lst[1:] if x>lst[0]]))


def anonymousFunctionMethod(filename):
    start_time=T.time()
    x = eval('['+open(filename ).readlines()[0]+']')
    x = quickSort(x)
    total = reduce(lambda x,y: x+y, [reduce(lambda x,y: x+y, [(j+1)*(ord(i)-
        64) for i in x[j]]) for j in xrange(len(x))])
    total_time=T.time()-start_time
    print "the name score sum of the file", filename, "is", total
    print "with anonymous functions and built in precompiled sort() method the program took", total_time, "seconds to run"


if __name__=="__main__":
    import sys
    nameScore(sys.argv[1])
    anonymousFunctionMethod(sys.argv[1])

