# Euler Problem 42:
# The nth term of the sequence of triangle numbers is given by
# t_n=(1/2)(n)(n+1); so the first ten triangle numbers are:
#   1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
#   By converting each letter in a word to a number corresponding to its
#   alphabetical position and adding these values we form a word value. For
#   example, the word value for SKY is 19 + 11 + 25 = 55 = t+10. If the word
#   value is a triangle number then we shall call the word a triangle word.
#
#   Using words.txt, a 16K file containing nearly two thousand common English
#   words, how many are triangle numbers?

# Solution:
# ---------------------------------------------------------
# Apart from the actual processing of the file and parsing into words we can
# either 1) Calculate each word value, then perform a computation to see if it
# is of the form (n(n+1))/2 or 2) store a reasonable number of the first n
# triangle numbers in a list, calculate the word value, then check to see if
# that word value is in the list of n triangle numbers that we generated. Ie no
# "common" English word is going to be longer than 25 characters and we can
# bound by all "z"s, 25*26 = 650. We would store all triangle numbers below 650
# in a relatively small list, calculate each word score then check if the score
# is in the list.
# Although the second method might be faster due to less "computations" in some
# way I usually prefer a more generic and scalable solution(maybe one day I'll
# want to see if random strings are triangle words?). We'll start with the
# scalable generic first methodology.

import time as T

def triangleNumbersInFile(filename):
    t_0 = T.time()
    triWordsFound = 0
    charDict = {'"':0,'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8,'I':9,'J':10,'K':11,'L':12,'M':13,'N':14,'O':15,'P':16,'Q':17,'R':18,'S':19,'T':20,'U':21,'V':22,'W':23,'X':24,'Y':25,'Z':26}
    wordsFile = open(filename, 'r')
    for word in wordsFile.read().split('","'): # Note that you get the first
        #and last " but this is ok we'll map to 0 in our character value dict
        wordScore = 0
        for char in word:
            wordScore += charDict[char]
        if isTriNum(wordScore):
            triWordsFound += 1
    t_1 = T.time()
    print "The number of Triangle Words found in", filename, "is:", triWordsFound
    print "This program took", t_1-t_0, "Seconds to run"


def isTriNum(num):
    #Using the closed formula for triangle numbers: 2T_n=n(n+1)
# => 2T_n=n^2+n => 8T_n=4n^2+4n => 8T_n+1=4n^2+4n+1 => 8T_n+1=(2n+1)^2
# So given an int x if (sqrt(8x+1)-1)/2 mod(1) == 0 then x is a triangle number
# (Note, you have to really use a tolerance with floats)
    if abs((((8.0*num+1)**.5)-1)/2)%1<.000001:
        return True
    else:
        return False

if __name__ == "__main__":
    import sys
    triangleNumbersInFile(sys.argv[1])


