#Checks if a number is "bouncy" i.e. non-monotonic digits Problem 112
def bouncy(n):
    if n <= 0:
        raise ValueError("Please enter a positive integer")
    #Trivial Case
    if n < 100:
        return False
    strnum = str(n)
    length = len(strnum)
    #Finding 1st digit that is different from the next (left to right)
    for i in range(length - 1):
        if strnum[i] != strnum[i + 1]:
            difference = int(strnum[i]) - int(strnum[i + 1])
            differentAt = i
            break
        else:
            difference = 0
    #Numbers where every digit is the same
    if difference == 0:
        return False
    else:
        isBouncy = False
        if difference < 0:
            for j in range(differentAt + 1, length - 1):
                if int(strnum[j]) > int(strnum[j + 1]):
                    isBouncy = True
                    break
        elif difference > 0:
            for j in range(differentAt + 1, length - 1):
                if int(strnum[j]) < int(strnum[j + 1]):
                    isBouncy = True
                    break
    return isBouncy
    
bouncyProportion = 0
num = 0
bouncyCount = 0
while bouncyProportion < 99:
    num += 1
    if bouncy(num):
        bouncyCount += 1
    bouncyProportion = (bouncyCount / num) * 100

print(num)