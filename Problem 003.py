from math import sqrt
from math import ceil

def pfactor(num):
    div = 1
    #remove multiples of 2
    while num % 2 == 0:
        div = 2
        num = num // 2
    if num == 1:
        return div
    #check whether each odd number up to sqrt divides the remaining number
    #if yes update largest divisor and make it the lower bound
    #if no such number, remaining number is prime
    while num != 1:
        i = max(3, div)
        while i <= ceil(sqrt(num)):
            if (num % i == 0):
                div = i
                num = num // div
            else:
                i += 2
        if num != 1:
            div = max(div, num)
            num = num // div
    return div

print(pfactor(600851475143))
