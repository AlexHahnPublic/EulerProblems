# Euler Problem 17:
# If the numbers 1 through 5 are written out in words: one, two, three, four,
# five then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
# If all the numbers from 1 to 1000 (one thousand) inclusive were written out
# in words, how many letters would be used?
#
#NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and
#forty-two) contains 23 letters and 115 (one hundred and fifteen)
# contains 20 letters. The use of "and" when writing out numbers is in
# compliance with British usage.

import math as M
import time as T

# The dictionary to reference number to number of letters in alph(num), note
# must include zero and count as 0 due to mod and floor function used later
dic = {0:0,1:3,2:3,3:5,4:4,5:4,6:3,7:5,8:5,9:4,10:3,11:6,12:6,13:8,14:8,15:7,16:7,17:9,18:8,19:8,20:6,30:6,40:5,50:5,60:5,70:7,80:6,90:6,100:10,200:10,300:12,400:11,500:11,600:10,700:12,800:12,900:11,1000:11}

def less100(x):
    if x <= 20:
        return dic[x]
    else:
        return dic[x%10]+ dic[int(M.floor(x/10)*10)]

def digAlphCount(n):
    start_time = T.time()
    total = 0
    for num in range(1,n+1):
        strRep = str(num)
        if len(strRep)<3:
            total += less100(int(num))
        elif num == 1000:
            total += 11
        elif num%100 == 0:
            total += dic[num]
        else:
            total += dic[M.floor(num/100)*100] + 3 + less100(num%100)
    total_time = T.time()-start_time
    print "The number of characters added together in the letter representations of 1 to", n, "is", total
    print "This program took", total_time, "seconds to run"



if __name__ == "__main__":
    import sys
    digAlphCount(int(sys.argv[1]))




