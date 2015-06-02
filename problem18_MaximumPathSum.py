# Euler Problem 18:
# By starting at the top of the triangle below and moving to adjacent numbers
# on the row below, the maximum total from top to bottom is 23.
#                       3
#                      7 4
#                     2 4 6
#                    8 5 9 3
#
# That is 3 + 7 + 4 + 9

# Find the maximum from top to bottom of the triangle below:
#                                      75
#                                    95  64
#                                  17  47  82
#                                18  35  87  10
#                              20  04  82  47  65
#                            19  01  23  75  03  34
#                          88  02  77  73  07  63  67
#                        99  65  04  28  06  16  70  92
#                      41  41  26  56  83  40  80  70  33
#                    41  48  72  33  47  32  37  16  94  29
#                  53  71  44  65  25  43  91  52  97  51  14
#                70  11  33  28  77  73  17  78  39  68  17  57
#              91  71  52  38  17  14  91  43  58  50  27  29  48
#            63  66  04  68  89  53  67  30  73  16  69  87  40  31
#          04  62  98  27  23  09  70  98  73  93  38  53  60  04  23
import time as T

def maxPath():
    start_time = T.time()
    triangleFile = open('triangle.txt')
    triangle = []

    for i in triangleFile:
        triangle.append([int(x) for x in i.strip().split() ])

    for row in range(1,len(triangle)):
        for col in range(len(triangle[row])):
            if col == 0:
                triangle[row][col] += triangle[row-1][col]
            elif col == len(triangle[row-1]):
                triangle[row][col] += triangle[row-1][col-1]
            else:
                triangle[row][col] += max(triangle[row-1][col],
                        triangle[row-1][col-1])
    total_time = T.time() - start_time
    print "The sum of the path adding to the largest total from top row to bottom row is:", max(triangle[len(triangle)-1])
    print "This program took", total_time,"seconds to run"

if __name__ == "__main__":
    maxPath()
