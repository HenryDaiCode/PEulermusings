from math import floor
#Replace with your filepath
lines = open("D:\Documents\Python\PEuler\Problem 13 data.txt").read().splitlines()
digitsum = []

for num in lines:
    i = 0
    while i < 50:
        if len(digitsum) < (i + 1):
            digitsum.append(int(num[49 - i]))
        else:
            digitsum[49 - i] += int(num[i])
        i += 1

for j in range(49):
    tempno = digitsum[j]
    tempunits = tempno % 10
    digitsum[j] = tempunits
    digitsum[j+1] += (tempno - tempunits) // 10
    
length = len(str(digitsum[49]))
if  length >= 10:
    finalno = str(digitsum[49])
    print(finalno[0 : 10])

k = 0
finalno = str(digitsum[49])
while k < (10 - length):
    finalno += str(digitsum[49 - k - 1])
    k += 1

print(finalno)