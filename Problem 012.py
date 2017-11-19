from math import sqrt
from math import ceil
#Returns nth triangle number
def tri(n):
    return ((n * n) + n) // 2

mostdivisors = 0
i = 1
while mostdivisors <= 500:
    halfdivisors = 0
    trinum = tri(i)
    for j in range(1, ceil(sqrt(trinum))):
        if trinum % j == 0:
            halfdivisors += 1
    divisors = 2 * halfdivisors
    if sqrt(trinum).is_integer():
        divisors += 1
    if divisors > mostdivisors:
        mostdivisors = divisors
    i += 1
#i - 1 to counterract last i += 1
print(tri(i - 1))