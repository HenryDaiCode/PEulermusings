import sys
i = 1
while i <= 1000:
    j = i + 1
    while j <= 1000:
        k = j + 1
        while k <= 1000:
            if (i * i) + (j * j) - (k * k) == 0:
                #print(i)
                #print(j)
                #print(k)
                if i + j + k == 1000:
                    print(i * j * k)
                    sys.exit()
            k += 1
        j += 1
    i += 1
                
                
                
                
                
                