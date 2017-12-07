#Finds reverse(n), i.e. 36 to 63 and checks if it is reversible (all odd digits)
def reversible(n):
    #No leading zeroes allowed in reverse(n)
    if n <= 0 or n % 10 == 0:
        return False
    digitlist = []
    #Extract digits into a list
    while (n > 0):
        digitlist.append(n % 10)
        n = n // 10
    length = len(digitlist)
    i = 0
    extra = 0
    while i < length:
        digitsum = digitlist[i] + digitlist[length - 1 - i] + extra
        if digitsum % 2 == 0:
            return False
        else:
            extra = digitsum // 10
        i += 1
    if extra == 0:
        return True
    elif extra % 2 == 1:
        return True
    else:
        return False
    
target = 10 ** 8
count = 0
for i in range(1, target):
    if reversible(i):
        count += 1
print(count)