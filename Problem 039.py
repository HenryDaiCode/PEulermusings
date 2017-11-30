from math import sqrt
#We will assume a <= b <= c
maxlength = 1000
perimeter = []
for n in range(1001):
    perimeter.append(0)
for a in range(1, maxlength):
    for b in range(a, maxlength):
        c = sqrt(a * a + b * b)
        if c.is_integer():
            if (a + b + c) <= 1000:
                perimeter[int(a + b + c)] += 1
mostperim = max(perimeter)
mostperims = [index for index, value in enumerate(perimeter) if value == mostperim]
print(mostperims)