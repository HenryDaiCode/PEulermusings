#Find nth digit of concatenating the positive integers
def ndigit(n):
    #9 digits for single digit numbers, 90 for double digit, 900 for triple digit etc...
    #Work out the size of the numbers we have to work with, variable i will be the number of digits of the numbers
    tempnum = n
    i = 0
    lowerorder = 0
    while tempnum > 0:
        i += 1
        #product is the number of digits at every digit level. 9 Single digit = 9, 90 Double digit = 180, ... etc
        product = (9 * (10 ** (i - 1))) * i
        tempnum -= product
        lowerorder += product
    #To reverse the final calculation that went over
    lowerorder -= product
    #Now to find the digit amongst the i-digit numbers
    n -= lowerorder
    #Look at the (position + 1)-th i-digit number
    position = (n - 1) // i
    num = (10 ** (i - 1)) + position
    #Which digit?
    digitindex = (n - 1) % i
    digit = str(num)[digitindex]
    return int(digit)

print(ndigit(1) * ndigit(10) * ndigit(100) * ndigit(1000) * ndigit(10000) * ndigit(100000) * ndigit(1000000))