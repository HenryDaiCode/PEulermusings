#Replace with your filepath
number = open("D:\Documents\Python\Problem 008 data.txt").read()
numberlist = []
for i in range(1000):
    numberlist.append(int(number[i]))

j = 0
product = 0
while j + 12 < 1000:
    tempprod = 1
    for k in range(13):
        tempprod *= numberlist[j + k]
    if tempprod > product:
        product = tempprod
    j += 1

print(product)