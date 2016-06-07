# Euler Problem 43:
# The number, 1406357289, is a 0 to 9 pandigital number because it is made up
# of each of the digits 0 to 9 in some order, but it also has a rather
# interesting sub-string divisibility property.
#
# Let d_1 be the first digit, d_2 be the second digit, and so on. In this way,
# we note the following:
#
# d_2d_3d_4=406 is divisible by 2
# d_3d_4d_5=063 is divisible by 3
# d_4d_5d_6=635 is divisible by 5
# d_5d_6d_7=357 is divisible by 7
# d_6d_7d_8=572 is divisible by 11
# d_7d_8d_9=728 is divisible by 13
# d_8d_9d_10=289 is divisible by 17
#
# Find the sum of all 0 to 9 pandigital numbers with this property.

# Solution:
# ---------------------------------------------------------
# So we know that there are 10!= ~4x10^6 permutations of the digits 0-9 (not
# that they'll be a decent portion less with all the leading zero values. Let's
# run through the permutations of the digits of 9876543210 checking for the
# prime divisibility criteria as we go.
#
# Note, creating, storing, then checking through that list takes much longer
# than one minute. I've checked the web and found several very significant
# speed ups where you apply a bit of divisor logic to drastically reduce the
# search space. See "problem43_SubStringDivisibility_MuchBetter.py". I'm
# leaving this in here because it has a nice recursive permutations generator

def checkPrimeDivis(strNum):
    if strNum[0] == 0:
        return False
# Collect the substring numbers to check prime divisors
    numStr1 = int(strNum[1:4])
    numStr2 = int(strNum[2:5])
    numStr3 = int(strNum[3:6])
    numStr4 = int(strNum[4:7])
    numStr5 = int(strNum[5:8])
    numStr6 = int(strNum[6:9])
    numStr7 = int(strNum[7:10])
# Check all criteria:
    if numStr1%2==0 and numStr2%3==0 and numStr3%5==0 and numStr4%7==0 and numStr5%11==0 and numStr6%13==0 and numStr7%17==0:
            return True
    else:
            return False

def allPerms(string, start, end):
    current = 0
    if start == end-1:
        if not string in result:
            result.append(string)
    else:
        for current in range(start, end):
            x = list(string)
            temp = x[start]
            x[start] = x[current]
            x[current] = temp
            allPerms(''.join(x), start+1, end)
            temp = x[start]
            x[start] = x[current]
            x[current] = temp

def main(inp):
    total = 0
    global result
    result = []
    allPerms(inp,0,len(inp))
    print len(result)
    #for perms in result:
        #if checkPrimeDivis(perms):
            #total += int(perms)
            #print "found one:", perms
    #print total


if __name__ == "__main__":
    import sys
    print main(str(sys.argv[1]))


