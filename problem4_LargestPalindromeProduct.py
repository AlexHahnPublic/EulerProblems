# Euler Problem 4:
# A palindrome number reads the same both ways. The largest palindrome made
# from the product of two 2-digit numbers is 9009= 91 x 99.
# Find the largest palindrome madefrom the product of two 3 digit numbers

# This problem is easy to brute force, we're more mature than that. My general
# approach is two start at 999*999 and while isPalindrome is false compute
# the next largest number. This is slightly harder than it sounds because
# coming up with a function/ iteration that gives the next largest number
# from the product of two numbers isn't exactly straightforward

import time

# Cheap Solution: calculate all the combinations/ products of 900-999 sort
# largest first, then check isPalendrome, (decrease by 100 each time)

# Recursive function isPalindrome to check if a number is a
# palindrome. Probably could be written a little cleaner but whatever
def isPalindrome(strnum):
    if len(strnum) == 1:
        return True
    elif len(strnum) == 2:
        if strnum[0] == strnum[1]:
            return True
        else:
            return False
    elif strnum[0] == strnum[len(strnum)-1]:
        return isPalindrome(strnum[1:len(strnum)-1])
    else:
        return False

# Only check 100+99+98+... =n numbers at a time, if a palindrome is found,
# stop
def findLargestPalindromeProduct_OkButNotGreat(n):
    orig = n
    start_time = time.time()
    palindromeFound = False
    while n > 0 and palindromeFound == False:
        lst = []
        #only check $\sum_{i=n}^{n+100}n$ at a time (999x999,999x998, etc)
        for i in range(n-99,n+1):
            for j in range(n-99,n+1):
                lst.append(i*j)
        uniqlst = set(lst)
        orderedlst = sorted(uniqlst)
        for num in orderedlst:
            if isPalindrome(str(num)):
                largestPalindromeProduct = num
                palindromeFound = True
        n = n-100
        total_time = time.time() - start_time
    print "The largest palindrome product of two numbers, both under", orig, "is", largestPalindromeProduct
    print " This program took:", total_time, "seconds to run"

#def findLargestPalindromeProduct_Analytic(n):
#    factor1 = n
#    factor2 = n
#    counter1 = 1
#    counter2 = 1
#    while factor1*factor2 != 0 #ispalindrome(factor1*factor2)
#        print "factor1 is: ", factor1, " factor2 is: ", factor2, "and their
#        product is: ", factor1*factor2
#        factor1 =
#        for i in range(counter1):

if __name__ == "__main__":
    import sys
    findLargestPalindromeProduct_OkButNotGreat(int(sys.argv[1]))



