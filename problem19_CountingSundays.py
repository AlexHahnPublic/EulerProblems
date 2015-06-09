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

import time

def numSundays():
    Day = [2,1,1,1901] # [DOW,DD,MM,YYYY]


def nextWeekDay(d):
    if d[0] % 7 == 0:
        d[0] = 1
    else:
        d[0] += 1
    print "The next day is:", d

def nextDay(d):
    if d[1] == 31:
        d = nextMonth(d)
        d[1] = 1
    elif d[1] = 30 and d[2] in [9,4,6,11]
        d = nextMonth(d)
        d[1] = 1
    elif d[2] == 2:
        if d[1] == 28 and d[3] % 4 == 0 and d[3] % 1000 == 400:
            d[1] += 1
        else


def nextMonth(d):
    if d[2] % 12 == 0:
        d[2] = 1
        d[3] += 1   # increment year if month is 12 -> 1
    else:
        d[2] += 1
    print "The next month is:", d



if __name__ == "__main__":
    import sys
    nextMonth([1,1,12,1901])


