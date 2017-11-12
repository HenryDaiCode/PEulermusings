#Replace with your filepath
numbers = open("D:\Documents\Python\PEuler\Problem 11 data.txt").read().split()

#converts array "coodinates" into the correct list index
def arrayconv(x, y):
    return ((x*20) + y)
    
def num(x, y):
    return int(numbers[arrayconv(x, y)])

greatestproduct = 0

#check rows
for i in range(17):
    for j in range(20):
        product = num(i, j) * num(i + 1, j) * num(i + 2, j) * num(i + 3, j)
        if product > greatestproduct:
            greatestproduct = product

#check columns
for i in range(20):
    for j in range(17):
        product = num(i, j) * num(i, j + 1) * num(i, j + 2) * num(i, j + 3)
        if product > greatestproduct:
            greatestproduct = product
        
#check diagonals
for i in range(17):
    for j in range(17):
        product = num(i, j) * num(i + 1, j + 1) * num(i + 2, j + 2) * num(i + 3, j + 3)
        if product > greatestproduct:
            greatestproduct = product
            
for i in range(17):
    for j in range(3, 20):
        product = num(i, j) * num(i + 1, j - 1) * num(i + 2, j - 2) * num(i + 3, j - 3)
        if product > greatestproduct:
            greatestproduct = product
            
print(greatestproduct)
