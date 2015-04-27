# Euler Problem 6:
# The sum of the squares of the first ten natural numbers is,
#       1^2+2^2+3^2+...+10^2 = 385
# The square of the sum of the first ten natural numbers is,
#       (1+2+3+...+10)^2 = 55^2 = 3025
# Hence the difference between the sum of the squares of the first ten natural
# numbers and the square of the sum is 3025 - 385 = 2640.
# Find the difference between the sum of the squares of the first one hundred
# natural numbers and the square of the sum.

def difOfSquares(n):
    sumOfSquares = 0
    squareOfSums = 0
    for i in range(1,n+1):
        sumOfSquares += i**2
        squareOfSums += i
    squareOfSums = squareOfSums**2
    difference = squareOfSums - sumOfSquares
    print difference

if __name__ == "__main__":
    import sys
    difOfSquares(int(sys.argv[1]))
