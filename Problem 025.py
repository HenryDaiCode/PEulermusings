fib1 = 1
fib2 = 1

i = 2
fib = 0
while len(str(fib)) < 1000:
    i += 1
    fib = fib1 + fib2
    fib1 = fib2
    fib2 = fib

print(i)