from math import sqrt
from math import ceil
#Function that returns the sum of a numbers proper divisors (code partially reused from Problem 023)
def divsum(n):
    if (not isinstance(n, int)) or (n <= 0):
        raise ValueError("Please enter a positive integer")
    #Takes care of special cases
    if n == 1:
        return 0
    elif n == 2:
        return 1
    divisors = set()
    divisors.add(1)
    for i in range(2, ceil(sqrt(n) + 1)):
        if n % i == 0:
            divisors.add(i)
            divisors.add(n // i)
    return sum(divisors)

#Amicable numbers i and j are numbers such that divsum(i) = j and divsum(j) = i and i != j
amicable = []
target = 10000
for i in range(2, target + 1):
    if i not in amicable:
        j = divsum(i)
        if divsum(j) == i and i != j:
            amicable.append(i)
            amicable.append(j)

print(sum(amicable))