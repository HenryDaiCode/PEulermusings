sum = 0
squaresum = 0
for i in range(1, 101):
    sum += i
    squaresum += (i * i)
    
print((sum * sum) - squaresum)