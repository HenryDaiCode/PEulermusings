def fracequal(frac1, frac2):
    if (frac1[0] * frac2[1]) == (frac1[1] * frac2[0]):
        return True
    return False
    
for i in range(10, 100):
    for j in range(i, 100):
        originalfrac = [i, j]
        a = i // 10
        b = i % 10
        c = j // 10
        d = j % 10
        if d != 0:
            if b < d and a == c:
                fracbd = [b, d]
                if fracequal(originalfrac, fracbd):
                    print("{} {}".format(originalfrac, fracbd))
            if a < d and b == c:
                fracad = [a, d]
                if fracequal(originalfrac, fracad):
                    print("{} {}".format(originalfrac, fracad))
        if b == d and not (b == 0 and d == 0):
            if a < c:
                fracac = [a, c]
                if fracequal(originalfrac, fracac):
                    print("{} {}".format(originalfrac, fracac))            
        if b > c and a == d:
            fracbc = [b, c]
            if fracequal(originalfrac, fracbc):
                print("{} {}".format(originalfrac, fracbc)) 