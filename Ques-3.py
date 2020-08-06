a = [0, 1, 0, 1, 0, 1, 1]
# sorting in linear time
count_0 = a.count(0)
count_1 = a.count(1)
for i in range(count_0 + count_1):
    if i < count_0:
        a[i] = 0
    else:
        a[i] = 1
print(a)
