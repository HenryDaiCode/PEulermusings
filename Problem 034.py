#Find the sum of all numbers which are equal to the sum of the factorial of their digits.
#Only need to test up to around 3 million as 9! = 362880
from math import factorial

totalsum = 0
for i in range(10, 3000000):
    #print(i)
    #Seems really inefficient, should probably use mod 10
    numstring = str(i)
    length = len(numstring)
    sum = 0
    for j in range(length):
        sum += factorial(int(numstring[j]))
    if sum == i:
        totalsum += i

print(totalsum)

#Final thoughts, could probably do the problem the other way round somehow, calculate all factorial sums