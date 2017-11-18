#Returns a boolean for whether digits in number are unique and a list of the digits
def digitlist(num):
    digitset = set()
    unique = True
    if num == 0:
        digitset.add(0)
        return (unique, digitset)
    while(num > 0):
        digit = num % 10
        if digit in digitset:
            unique = False
        digitset.add(digit)
        num = num // 10
    return (unique, digitset)

#Set an upper limit for the numbers to multiply
limit = 10000
productset = set()
for i in range(limit):
    numi = digitlist(i)
    if (numi[0] == True) and (0 not in numi[1]):
        for j in range(limit):
            numj = digitlist(j)
            if (numj[0] == True) and (0 not in numj[1]):
                if numi[1].isdisjoint(numj[1]):
                    product = i * j
                    digitprod = digitlist(product)
                    union = numi[1] | numj[1]
                    if (digitprod[0] == True) and (0 not in digitprod[1]) and (digitprod[1].isdisjoint(union)):
                        totalunion = union | digitprod[1]
                        if len(totalunion) == 9:
                            print("{} {} {}".format(i, j, product))
                            productset.add(product)
                            
print(sum(productset))