primes = [2]
i = 3
while len(primes) < 10001:
    isprime = True
    for p in primes:
        if i % p == 0:
            isprime = False
            break
    if isprime:
        primes.append(i)
    i += 2
    
print(primes[len(primes) - 1])