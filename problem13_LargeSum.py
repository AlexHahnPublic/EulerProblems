# Euler Problem 13:
# Work out the first ten digits of the following one-hundred 50-digit numbers.
#
# Place holder for list
#
# Or just open the file:

import time as T

def largeSum(data):
    start_time = T.time()

    # using a nice list comprehension
    total = sum([int(line[:11]) for line in open(data).readlines()])

    # Don't actually need to use strip() but I'm leaving it in for reference
    #total = sum([int(line.strip()[:11]) for line in open(data).readlines()])
    ans = str(total)[:10]   # chop off any extra digits
    total_time = T.time()-start_time
    print "The first ten digits of the sum of the numbers read in from file", data, "is", ans
    print "This program took", total_time, "seconds to run"


# Honestly they're about the same... maybe will test on a huge file later
def largeSum2(data):
    start_time = T.time()

    # using a running total (might be faster if the file is HUGE and our
    # previous function
    total = 0
    for line in open(data):
        total += int(line[:11])
    ans = str(total)[:10]   # chop off any extra digits
    total_time = T.time()-start_time
    print "The first ten digits of the sum of the numbers read in from file", data, "is", ans
    print "This program took", total_time, "seconds to run"




if __name__ == "__main__":
    import sys
    largeSum(sys.argv[1])















