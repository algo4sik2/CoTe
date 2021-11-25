table = list()
for i in range(10):
    table.append(list(map(int, input().split())))
i, j = 1, 1
while table[i][j] != 2:
    table[i][j] = 9
    if table[i][j + 1] != 1:
        j = j + 1
    elif table[i + 1][j] != 1:
        i = i + 1
    else:
        break

table[i][j] = 9
for y in range(10):
    for x in range(10):
        print(table[y][x], end=' ')
    print()

