# Euler Problem 19:
# You are given the following information, but you may wish to do some research
# for yourself.
#       - 1 Jan 1900 was a Monday.
#       - Thirty days has September,
#         April, June, and November.
#         All the rest have thirty-one,
#         Saving February alone,
#         Which has twenty-eight, rain or shine.
#         And on leap years twenty-nine.
#       - A leap year occurs on any year evenly divisible by 4, but not on a
#       century unless it is evenly divisible by 400.

# How many Sundays fell on the first of the month during the 20th century (1
# Jan 1901 to 31 Dec 2000)?

import time as T

def numSundaysOnFirst():
    start_time = T.time()
    Day = [2,1,1,1900] # [DOW,DD,MM,YYYY]
    counter = 0
    while Day[3] != 2001:
        Day = nextDay(Day)
        if Day[0] == 1 and Day[1] == 1 and Day[3] != 1900:
            counter += 1
    total_time = T.time() - start_time
    print "There are", counter, "Sundays that fell on the first of the month during the 20th century"
    print "This program took", total_time, "seconds to run"



def nextWeekday(d):
    if d[0] % 7 == 0:
        d[0] = 1
    else:
        d[0] += 1
    return d

def nextYear(d):
    d[3] += 1
    return d

def nextMonth(d):
    if d[2] % 12 == 0:
        d[2] = 1
        d = nextYear(d)     # increment year if month is 12 -> 1
    else:
        d[2] += 1
    return d

def nextDay(d):
    if d[1] == 31:
        d = nextMonth(d)
        d[1] = 1
    elif d[1] == 30 and d[2] in [9,4,6,11]:
        d = nextMonth(d)
        d[1] = 1
    elif d[2] == 2:
        if d[1] == 29:
            d = nextMonth(d)
            d[1] = 1
        elif d[1] == 28 and d[3] % 4 != 0:
            d = nextMonth(d)
            d[1] = 1
        elif d[1] == 28 and d[3] % 100 == 0:
            if d[3] % 400 != 0:
                d = nextMonth(d)
                d[1] = 1
            else:   # it's  leap year that's divisible by 400
                d[1] += 1
        else:   # it's a leap year that's not divisible by 100
            d[1] += 1
    else:       # it's a day before the 28th
        d[1] += 1
    d = nextWeekday(d)
    return d

if __name__ == "__main__":
    import sys
    numSundaysOnFirst()


