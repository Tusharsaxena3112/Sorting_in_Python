# Find the largest possible number can be formed from the given set.

a = [54, 546, 548, 60]
num = a[0]
for i in range(1, len(a)):
    if int(str(num) + str(a[i])) > int(str(a[i]) + str(num)):
        num = int(str(num) + str(a[i]))
    else:
        num = int(str(a[i]) + str(num))
print(num)

# 6054854654
