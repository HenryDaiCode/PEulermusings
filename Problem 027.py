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
    return primes

primelist = primes(1000000)
maxprimes = 0
abmax = [0, 0]
for a in range(-1000, 1001):
    for b in range(-1000, 1001):
        isPrime = True
        n = 0
        while isPrime:
            sum = (n * n) + (a * n) + b
            if not sum in primelist:
                isPrime = False
            else:
                n += 1
        if n > maxprimes:
            maxprimes = n
            abmax[0] = a
            abmax[1] = b
            
print(abmax)