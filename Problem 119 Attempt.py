def ispower(num, power):
    if power == 1:
        return False
    while num > 1:
        num = num / power
        if not num.is_integer():
            break
    if num == 1:
        return True
    return False

def digitsum(num):
    sum = 0
    stringnum = str(num)
    for i in range(len(stringnum)):
        sum += int(stringnum[i])
    return sum

specialnum = []
i = 10
while len(specialnum) < 30:
    if ispower(i, digitsum(i)):
        specialnum.append(i)
        print(i)
    i += 1
    
print(specialnum[29])