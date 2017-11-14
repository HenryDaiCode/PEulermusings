from sympy import prime
target = 10 ** 10
remainder = 0
#to have big remainders you need big numbers
n = 20001
while remainder <= target:
    #every other remainder is 2
    n += 2
    primen = prime(n)
    #sum = ((primen - 1) ** n) + ((primen + 1) ** n)
    #use binomial theorem to optimise
    remainder = 2 * n * primen
    print(remainder)
    
print(n)