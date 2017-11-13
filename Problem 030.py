sum = 0
for i in range(2, 1000000):
    length = len(str(i))
    powersum = 0
    for j in range(length):
        powersum += int(str(i)[j]) ** 5
    if powersum == i:
        sum += powersum

print(sum)