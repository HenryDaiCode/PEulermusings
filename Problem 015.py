#Calculates n choose k
from math import factorial
def comb(n, k):
    if (n > 0) and (k >= 0) and (n >= k):
        return factorial(n) // (factorial(k) * factorial(n - k))
    
print(comb(40, 20))