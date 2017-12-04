def digitsum(n):
    sum = 0
    while(n > 0):
        digit = n % 10
        sum += digit
        n = n // 10
    return sum
    
maxsum = 0
target = 100
for i in range(1, target):
    for j in range(1, target):
        print("{} {}".format(i, j))
        num = i ** j
        tempsum = digitsum(num)
        if maxsum < tempsum:
            maxsum = tempsum

print(maxsum)