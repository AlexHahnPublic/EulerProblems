# Euler Problem :
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we
# get 3, 5, 6, and 9. The sum of these multiples is 23

# Find the sum of all the multiples of 3 and 5 below 1000.

def sum3and5(n):
    total = 0
    for nat in range(n):
        if (nat % 3 == 0) or (nat % 5 == 0):
            total = total + nat
    print total

if __name__ == "__main__":
    import sys
    sum3and5(int(sys.argv[1]))

