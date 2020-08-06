# 1 - Sort the array having two elements placed wrongly

a = [1, 2, 4, 3, 5, 6]
c = 0
for i in range(1, len(a) - 2):
    if a[i - 1] > a[i + 1]:
        c += 1
        a[i - 1], a[i + 1] = a[i + 1], a[i - 1]
print(a)
print(c)
