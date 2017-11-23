#A number n is called abundant if the sum of its proper divisors (1 included, not itself) exceeds n.
#Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
from math import sqrt
from math import ceil
#Function that returns a list of the proper divisors of a number
def pdiv(n):
    if (not isinstance(n, int)) or (n <= 0):
        raise ValueError("Please enter a positive integer")
    divisors = set()
    divisors.add(1)
    #Takes care of special case
    if n == 2:
        return divisors
    for i in range(2, ceil(sqrt(n) + 1)):
        if n % i == 0:
            divisors.add(i)
            divisors.add(n // i)
    return divisors

#Function that returns an ordered list of abundant numbers under n
def abundant(n):
    if (not isinstance(n, int)) or (n <= 0):
        raise ValueError("Please enter a positive integer")
    abundantlist = []
    for i in range(1, n):
        divisors = pdiv(i)
        if sum(divisors) > i:
            abundantlist.append(i)
    abundantlist.sort()
    return abundantlist

#Function that takes two ordered list of odd and even integers and another integer and checks if there is any pair of integers in either of the two lists that sum to the other integer
def sumcheck(oddlist, evenlist, n):
    oddlength = len(oddlist)
    evenlength = len(evenlist)
    #Find the relative position of n in the two lists
    oddmax = 0
    if n >= oddlist[oddlength - 1]:
        oddmax = oddlength
    else:
        while n >= oddlist[oddmax]:
            oddmax += 1
    evenmax = 0
    if n >= evenlist[evenlength - 1]:
        evenmax = evenlength
    else:
        while n >= evenlist[evenmax]:
            evenmax = min(evenmax + 5, evenlength - 1)
    #There are vastly fewer abundant odd numbers less than 29000, so we will treat odd and even cases separately
    #Odd Cases
    if n % 2 == 1:
        for i in range(oddmax):
            inum = oddlist[i]
            if inum > n:
                break
            for j in range(evenmax):
                jnum = evenlist[j]
                if jnum > n:
                    break
                sum = inum + jnum
                if sum == n:
                    return True
                elif sum > n:
                    break
        return False
    
    #Even Cases
    for i in range(oddmax):
        inum = oddlist[i]
        if inum > n:
            break
        for j in range(oddmax):
            jnum = oddlist[j]
            if jnum > n:
                break
            sum = inum + jnum
            if sum == n:
                return True
            elif sum > n:
                break
    for i in range(evenmax):
        inum = evenlist[i]
        if inum > n:
            break
        for j in range(evenmax):
            jnum = evenlist[j]
            if jnum > n:
                break
            sum = inum + jnum
            if sum == n:
                return True
            elif sum > n:
                break
    return False

#We are given that numbers greater than 28123 can always be written as a sum of 2 abundant numbers    
abuno = abundant(28124)
oddlist = []
evenlist = []
for num in abuno:
    if num % 2 == 1:
        oddlist.append(num)
    evenlist.append(num)
isNotAbunoSum = []
for i in range(1, 28124):
    if not sumcheck(oddlist, evenlist, i):
        isNotAbunoSum.append(i)
print(sum(isNotAbunoSum))