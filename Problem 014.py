longest = 0
longestnum = 0
for i in range(1, 1000001):
    length = 1
    num = i
    while num != 1:
        if num % 2 == 0:
            num = num // 2
        else:
            num = (3 * num) + 1
        length += 1
    if length > longest:
        longest = length
        longestnum = i

print("{} with {} terms".format(longestnum, longest))