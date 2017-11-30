rangelist = range(2, 101)
distinctab = set()
for a in rangelist:
    for b in rangelist:
        distinctab.add(a ** b)

print(len(distinctab))