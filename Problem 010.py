#Find primes less than n via sieve of Eratosthenes
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

sum = 0    
for prime in primes(2000000):
    sum += prime

print(sum)