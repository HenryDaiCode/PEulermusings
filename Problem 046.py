#It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square. We want to find the smallest odd counterexample.

#Find primes less than n via sieve of Eratosthenes code borrowed from Problem 010
from math import ceil
from math import sqrt
def primes(n):
    nset = set()
    removed = set()
    #Taking care of trivial cases
    if n <= 2:
        return
    elif n == 3:
        nset.add(2)
        return nset
        
    for i in range(2, n):
        nset.add(i)
    j = 2
    
    while j <= ceil(sqrt(n)):
        if not j in removed:
            multiplej = j + j
            while multiplej <= n:
                removed.add(multiplej)
                multiplej += j
        j += 1
    
    primes = nset - removed
    primes = list(primes)
    primes.sort()
    return primes

#Find squares up to n
def squares(n):
    squarelist = []
    i = 1
    while i * i <= n:
        squarelist.append(i * i)
        i += 1
    return squarelist
    
primelist = primes(2500000)
squarelist = squares(2500000)
for i in range(3, 2000000, 2):
    if i not in primelist:
        print(i)
        noSumFound = True
        j = 0
        while primelist[j] < i and noSumFound:
            primej = primelist[j]
            k = 0
            while squarelist[k] < i:
                squarek = squarelist[k]
                sum = primej + (2 * squarek)
                if sum == i:
                    noSumFound = False
                    break
                elif sum > i:
                    break
                k += 1
            j += 1
        if noSumFound:
            print("{} found".format(i))
            break