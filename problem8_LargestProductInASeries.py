# Euler Problem 8:
# The four adjacent digits in the 1000-digit number that have the greatest
# product are 9x9x8x9=5832
#       number place holder

#Find the thirteen adjacent digits in the 1000-digit number that have the
# greatest product. What is the value of this product?

# Solution:
# I think the best way to go about this is just to check the product of
# the first 13 digits, then 2 to 14 digits, and so on and replace the
# largest prod value if a bigger one is found. The only other thing I
# could think about but I don't believe is worth the extra coding is if
# you chop the number (string input) wherever there's a zero, then throw
# out all strings less than length 13, and among those remaining run the
# previously described method. This may improve things whenever the
# distribution of zero's is pretty much even for every 13 digits (or more?
# too many zero's? not really worth the dev work either way).

import time

def largestProduct(n):
    start_time = time.time()
    largestProd = 0
    startIndex = 0
    while startIndex < len(n)-12:
        prod = 1
        numStr = n[startIndex:startIndex+13]
        for num in numStr:
            prod *= int(num)
        if prod > largestProd:
            largestProd = prod
            mults = numStr
        startIndex += 1
    total_time = time.time() - start_time
    print "The largest 13 digit product is:", largestProd
    print "It is the multiplication of:", mults
    print "This program took", total_time, "seconds to run"

if __name__ == "__main__":
    import sys
    largestProduct(sys.argv[1])

