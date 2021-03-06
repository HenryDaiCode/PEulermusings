#A more efficient implementation of the sieve.
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