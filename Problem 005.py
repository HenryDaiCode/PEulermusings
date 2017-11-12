def gcd(num1, num2):
    div = 1
    for i in range(1, min(num1, num2) + 1):
        if (num1 % i == 0) and (num2 % i == 0):
            div = i
    return div

lcm = 1    
for i in range(1, 21):
    midgcd = gcd(lcm, i)
    lcm = (lcm * i) // midgcd
    
print(lcm)
