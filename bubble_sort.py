l = [1, 3, 5, 1, 4, 1]

for i in range(len(l)):
    for j in range(1, len(l)):
        if l[j - 1] > l[j]:
            l[j - 1], l[j] = l[j], l[j - 1]
print(l)
