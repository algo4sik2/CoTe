# 3

h, w = map(int, input().split())
table = []
seg = 0
for _ in range(h):
  row = list(map(int, list(input())))
  table.append(row)

i, j = 0,0

def fill(i, j):
  table[i][j] = 1
  check(i, j)
  

def check(i, j):
  if i > 0 and table[i - 1][j] == 0:
    fill(i - 1, j)
  if j > 0 and table[i][j - 1] == 0:
    fill(i, j - 1)
  if i < h - 1 and table[i + 1][j] == 0:
    fill(i + 1, j)
  if j < w - 1 and table[i][j + 1] == 0:
    fill(i, j + 1)


for i in range(h):
  for j in range(w):
    if table[i][j] == 0:
      k, l = i, j
      check(k, l)
      seg += 1
      print(k, l, seg)
   
    
print(seg)


# 4

h, w = map(int, input().split())
table = []

for _ in range(h):
  table.append(list(map(int, input())))

shortest = h * w

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

def bfs(a, b, cnt):
  cnt += 1
  if a == h - 1 and b == w - 1:
    global shortest
    shortest = shortest if shortest <= cnt else cnt
  table[a][b] == 2
  for idx in range(4):
    y, x = a + dy[idx], b + dx[idx]
    if 0 <= y <= h - 1 and 0 <= x <= w - 1:
      if table[y][x] == 1:
        table[y][x] = 2
        bfs(y, x, cnt)
      
bfs(0, 0, 0)

print(shortest)