from math import ceil
from math import sqrt
from sys import exit
#Function from Problem 010
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
    
primelist = list(primes(1000000))
primelist.sort()
length = len(primelist)
sumlen = 600
while sumlen > 0:
    i = 0
    while i + sumlen < length:
        sum = 0
        for j in range(i, i + sumlen):
            sum += primelist[j]
        if sum > 1000000:
            break
        if sum in primelist:
            print("{} which is a sum of {} consecutive primes".format(sum, sumlen))
            exit()
        i += 1
    sumlen -= 1