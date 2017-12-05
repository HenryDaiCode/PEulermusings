from math import factorial
def comb(n, r):
    return factorial(n) // (factorial(r) * factorial(n - r))
    
overMillion = 0
for n in range(101):
    for r in range(n + 1):
        if comb(n, r) > 1000000:
            overMillion += 1
            
print(overMillion)
