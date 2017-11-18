num = 2 ** 1000
sum = 0
while(num > 0):
    digit = num % 10
    sum += digit
    num = num // 10
    
print(sum)