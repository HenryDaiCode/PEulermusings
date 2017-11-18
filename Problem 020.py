from math import factorial
num = factorial(100)
sum = 0
while(num > 0):
    digit = num % 10
    sum += digit
    num = num // 10
    
print(sum)