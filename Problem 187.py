#Implementation of sieve of Eratosthenes borrowed from Problem 010
from math import ceil
from math import sqrt
def primes(n):
    #Taking care of trivial cases
    if n <= 2:
        return []
    elif n == 3:
        return [2]
    numbers = [False, False]
    for i in range(2, n + 1):
        numbers.append(True)
    j = 2
    while j <= ceil(sqrt(n)):
        square = j * j
        if numbers[j]:
            multiplej = square
            while multiplej <= n:
                numbers[multiplej] = False
                multiplej += j
        j += 1
    primelist = [index for index, boolean in enumerate(numbers) if boolean == True]
    return primelist
    
primelist = primes(50000000)
#Know all products of 2 with another prime < 50 million are less than 10^8. So start counting from 3.
length = len(primelist)
count = length
primelist = primelist[1:]

isDone = False
while not isDone:
    currentPrime = primelist[0]
    if currentPrime * currentPrime >= 10 ** 8:
        isDone = True
    else:
        length = len(primelist)
        upperbound = length - 1
        while currentPrime * primelist[upperbound] >= 10 ** 8:
            upperbound -= 1
        count += (upperbound + 1)
        primelist = primelist[1:upperbound + 1]
print(count)