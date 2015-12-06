# Euler Problem 32:
# We shall say that an n-digit number is pandigital if it makes use of all the
# digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1
# through 5 pandigital.

# The product 7254 is unusual, as the identity, 39 x 186 = 7254, containing
# multiplicand, multiplier, and product is 1 through 9 pandigital.

# Find the sum of all products whose multiplicand/ multiplier/ product identity
# can be written as a 1 through 9 pandigital.

# Hint: Some products can be obtained in more than one way so be sure to only
# include it once in your sum.

# Solution
# -----------------------------------------------

# Let's first attack this with a brute force method. First let's right a helper
# function to check if a number is pandigital:

def isPandigital(n):
    strRep=str(n)
    check=[0]*10
    # First check length
    if len(strRep) != 10:
        return False
    # Check digits for 0-9 span and no reps
    strRep=str(n)
    for dig in strRep:
        if check[int(dig)]==1:
            return False
        else:
            check[int(dig)]=1
    return True

def catOfTerms(x,y):
    return str(x)+str(y)+str(x*y)

def allPandigitalNums():
    pans=[]
    for i in xrange(0,9876):
        for j in xrange(i,10000/i99876):
 #           print "checking",i,"x",j
            num=catOfTerms(i,j)
            if isPandigital(num):
                    pans.append(num)
    ans=sum(set(pans))
    print "pandig numbers are",pans
    print "answer is", ans


# One Liner
def oneLiner():
    import time as  T
    start_time=T.time()
    print "The sum of all products whose multiplicand, multiplier and product identity can be written as 1-9 pandigital is:"
    print sum(set(map(lambda x: int(x[0:4]),filter(lambda x:sorted([i for i in x]) == map(str,range(1,10)),[str(a*b)+str(a)+str(b) for a in range(1,2000) for b in range(1,100)]))))
    print "This program took", T.time()-start_time, "seconds to run"



if __name__== "__main__":
    oneLiner()











