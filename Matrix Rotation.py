matrix = [[1, 2, 3, 4], [2, 3, 4, 5], [2, 4, 5, 6], [2, 3, 4, 5]]
m = 4
n = 4
layers = [2, 2]
# 1 2 3 18
# 4 5 6 16
# 7 8 9 15
mat = []
for i in range(len(layers)):
    temp = []
    for j in range(i, n - 1 - i):
        temp.append(matrix[i][j])
    for j in range(i, m - 1 - i):
        temp.append(matrix[j][n - 1 - i])
    for j in range(n - 1 - i, i, -1):
        temp.append(matrix[m - 1 - i][j])
    for j in range(m - 1 - i, i, -1):
        temp.append(matrix[j][i])

    mat.append(temp)

for i in range(len(layers)):
    row = mat[i]
    if (i + 1) % 2 == 0:
        idx = len(row) - layers[i]
    else:
        idx = layers[i] % len(row)
    for j in range(i, n - 1 - i):
        matrix[i][j] = row[idx]
        idx = (idx + 1) % len(row)
    for j in range(i, m - 1 - i):
        matrix[j][n - 1 - i] = row[idx]
        idx = (idx + 1) % len(row)
    for j in range(n - 1 - i, i, -1):
        matrix[m - 1 - i][j] = row[idx]
        idx = (idx + 1) % len(row)
    for j in range(m - 1 - i, i, -1):
        matrix[j][i] = row[idx]
        idx = (idx + 1) % len(row)

for row in matrix:
    print(*row)
