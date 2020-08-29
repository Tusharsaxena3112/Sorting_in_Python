n = int(input())
l = []
s = []
for i in range(n):
    l.append(list(map(int, input().split())))
for i in range(n):
    for j in range(n):
        s.append(l[i][j])
d = ''
for i in s:
    if str(i) not in d:
        print(f"{i} comes {s.count(i)}")
        d += str(i)
