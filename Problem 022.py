#Replace with your filepath        
names = open("D:\Documents\Python\PEuler\Problem 022 data.txt").read().split(",")
names = [i.replace('"', '') for i in names]
names.sort()
dictionary = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8, "I": 9, "J": 10, "K": 11, "L": 12, "M": 13, "N": 14, "O": 15, "P": 16, "Q": 17, "R": 18, "S": 19, "T": 20, "U": 21, "V": 22, "W": 23, "X": 24, "Y": 25, "Z": 26}
totalscore = 0
for name in names:
    length = len(name)
    index = names.index(name) + 1
    lettersum = 0
    for j in range(length):
        lettersum += dictionary.get(name[j])
    totalscore += (lettersum * index)
    
print(totalscore)