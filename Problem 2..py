def evenfib(upperbound):
    if upperbound <= 2:
        sum = 0
    num1 = 1
    num2 = 2
    sum = 2
    while (num1 + num2) <= upperbound:
        num3 = num1 + num2
        if ((num3) % 2) == 0:
            sum += num3
        num1 = num2
        num2 = num3
    return sum

print(evenfib(4000000))