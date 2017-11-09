def palincheck(num):
    if not isinstance(num, int):
        raise ValueError("Please enter an integer")
    string = str(num)
    length = len(string)
    checkno =  length // 2
    for i in range(checkno):
        if string[i] != string[length - 1 - i]:
            return False
    return True
    
threedigit = range(100, 1000)
highestpalin = 0
for i in threedigit:
    for j in threedigit:
        product = i * j
        if palincheck(product):
            highestpalin = max(highestpalin, product)

print(highestpalin)