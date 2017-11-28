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

#Returns a list of all cyclic permutations of a number
def cyclic(n):
    digitlist = []
    numberlist = []
    #Have to remember we are storing the digits "backwards"
    while(n > 0):
        digitlist.append(n % 10)
        n = n // 10
    length = len(digitlist)
    cyclicCounter = 0
    while cyclicCounter < length:
        digitCounter = length - 1
        number = 0
        i = length - cyclicCounter - 1
        while i >= 0:
            number += digitlist[i] * (10 ** digitCounter)
            digitCounter -= 1
            i -= 1
        j = length - 1
        while j > length - cyclicCounter - 1:
            number += digitlist[j] * (10 ** digitCounter)
            digitCounter -= 1
            j -= 1
        numberlist.append(number)
        cyclicCounter += 1
    return numberlist

primelist = primes(1000000)
primelistcopy = primelist[:]
circPrimeCount = 0
for prime in primelist:
    if prime in primelistcopy:
        isCircularPrime = True
        cyclicList = cyclic(prime)
        for permutation in cyclicList:
            if permutation not in primelistcopy:
                isCircularPrime = False
                break
        if isCircularPrime:
            cyclicSet = set(cyclicList)
            circPrimeCount += len(cyclicSet)
            for cprime in cyclicSet:
                primelistcopy.remove(cprime)
        else:
            primelistcopy.remove(prime)
print(circPrimeCount)