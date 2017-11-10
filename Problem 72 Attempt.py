from math import gcd

class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
        
    def reducecheck(self):
        if gcd(self.numerator, self.denominator) == 1:
            return True
        return False
        
    def display(self):
        print("{num} {denom}".format(num = self.numerator, denom = self.denominator))

fraclist = []
for i in range(2, 10000001):
    for j in range(1, i):
        frac = Fraction(j, i)
        if frac.reducecheck():
            #frac.display()
            fraclist.append(frac)

print(len(fraclist))
        