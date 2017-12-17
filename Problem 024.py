import itertools
digitlist = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
count = 0
# prevNum = 0
# currentNum = 0
numlist = []
emptystr = ""
for comb in itertools.permutations(digitlist):
    num = int(emptystr.join(comb))
    if count < 1000000:
        numlist.append(num)
        count += 1
    elif count == 1000000:
        numlist.sort()
        count += 1
    else:
        if num < numlist[999999]:
            numlist.append(num)
numlist.sort()
print(numlist[999999])
        