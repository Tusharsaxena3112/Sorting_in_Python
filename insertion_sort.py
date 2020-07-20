l = [2, 4, 3, 1, 5]

for i in range(1, len(l)):
    m = l[i]
    j = i
    while j > 0 and l[j - 1] > m:
        l[j] = l[j - 1]
        j -= 1
    l[j] = m
print(l)
