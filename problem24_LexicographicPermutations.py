# A permutation is an ordered arrangement of objects. For example, 3124 is one
# possible permutation of the digits 1, 2, 3, and 4. If all of the permutations
# are listed numerically or alphabetically, we call it lexicographic order. The
# lexicographic permutations of 0, 1, and 2 are:

#       012, 021, 102, 120, 201, 210

# What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4,
# 5, 6, 7, 8, and 9?

#TODO Figure out the number theoretic way (using n!) that's detailed on euler

import time as T

def findK(lst):
    k=len(lst)-1
    while k!= 0:
        if lst[k-1]<lst[k]:
            return k-1
        k-=1
    print 'no more lexicographic permutations'

def findL(lst,k):
    l=len(lst)-1
    while l != k:
        if lst[l]>lst[k]:
            return l
        else:
            l -= 1

def permute(lst):
    lenlst=len(lst)
    k = findK(lst)
    l = findL(lst,k)
    temp=lst[k]
    lst[k]=lst[l]
    lst[l]=temp
    nlst=lst[:k+1]
    for i in range(lenlst-(k+1)):
        nlst = nlst + [lst[lenlst-(i+1)]]
    return nlst

def nthLexPerm(num):
    st = T.time()
    lst = [0,1,2,3,4,5,6,7,8,9]
    counter = 1
    while counter != num:
        lst = permute(lst)
        counter += 1
    tt = T.time()-st
    print 'The', num, 'th lexicographic permutation is:', lst
    print 'This program took', tt, 'seconds to run'

if __name__=="__main__":
    import sys
    nthLexPerm(int(sys.argv[1]))

