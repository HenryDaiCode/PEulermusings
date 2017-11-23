#Counts the number of letters needed to write a number in standard English from 1 up to 9999
def lettercount(n):
    dict = {1: 3, 2: 3, 3: 5, 4: 4, 5: 4, 6: 3, 7: 5, 8: 5, 9: 4, 10: 3, 11: 6, 12: 6, 13: 8, 14: 8, 15: 7, 16: 7, 17: 9, 18: 8, 19: 8, 20: 6, 30: 6, 40: 5, 50: 5, 60: 5, 70: 7, 80: 6, 90: 6, 100: 7, 1000: 8}
    if (not isinstance(n, int)) or (n > 9999) or (n <= 0):
        raise ValueError("Please enter a positive integer less than 10000")
    thousandcount = 0
    hundredcount = 0
    tenscount = 0
    total= 0
    while n - 1000 >= 0:
        n -= 1000
        thousandcount += 1
    if thousandcount > 0:
        total += (dict[thousandcount] + dict[1000])
    while n - 100 >= 0:
        n -= 100
        hundredcount += 1
    if hundredcount > 0:
        total += (dict[hundredcount] + dict[100])
    if n == 0:
        return total
    elif n < 20:
        #Remember to add in "and" if number is greater than 100
        if total > 0:
            total += (3 + dict[n])
        else:
            total += dict[n]
    else:
        while n - 10 >= 0:
            n -= 10
            tenscount += 1
        if total > 0:
            total += (3 + dict[tenscount * 10])
        else:
            total += dict[tenscount * 10]
        if n > 0:
            total += dict[n]
    return total    

total = 0
for i in range (1, 1001):
    total += lettercount(i)
print(total)