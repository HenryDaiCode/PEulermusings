from math import floor
def sumdivis(num, upperbound):
    if num <= 0 or upperbound <= 0:
        raise ValueError("Please input a positive multiple and upperbound")
    #upperbound - 1 to take care of case where upperbound is divisible by num because we want strictly less
    quotient = floor((upperbound - 1) / num)
    realupper = num * quotient
    total = int(((num + realupper) * quotient) / 2)
    return total

print(sumdivis(3, 1000) + sumdivis(5, 1000) - sumdivis(15, 1000))
