from math import log
#Compares a^b and c^d and returns which is larger
def compare(a, b, c, d):
    if b * log(a) >= d * log(c):
        return [a, b]
    return [c, d]

numbers = []
#Replace with your filepath
with open("D:\Documents\Python\PEuler\Problem 099 data.txt") as file:
    for line in file:
        numbers += line.rstrip("\n").split(",")
largestnum = [1, 0]
largestindex = -1
for i in range(1000):
    result = compare(largestnum[0], largestnum[1], int(numbers[i * 2]), int(numbers[(i * 2) + 1]))
    if result != largestnum:
        largestnum = result
        largestindex = i + 1
print(largestindex)