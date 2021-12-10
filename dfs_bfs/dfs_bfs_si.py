# 실전문제 3 음료수 얼려 먹기(p.149)
from collections import deque
import sys
sys.stdin = open("input.txt", "r")

n, m = map(int, input().split())
info = []
for i in range(n):
    info.append(list(map(int, input())))

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
cnt = 0

def dfs(x, y):
    info[x][y] = 2
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if info[nx][ny] == 0:
                dfs(nx, ny)

def bfs(a, b):
    q = deque([(a, b)])
    info[a][b] = 2
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if info[nx][ny] == 0:
                    info[nx][ny] = 2
                    q.append((nx, ny))

for i in range(n):
    for j in range(m):
        if info[i][j] == 0:
            bfs(i, j)    # dfs(i, j)도 가능합니다
            cnt += 1

print(cnt)

#-----------------------------------------#


# 실전문제 4 미로 탈출(p.152)
from collections import deque
import sys
sys.stdin = open("input.txt", "r")

n, m = map(int, input().split())
info = []
for i in range(n):
    info.append(list(map(int, input())))

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def bfs(x, y):
    q = deque([(x, y)])
    info[x][y] = 2
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if info[nx][ny] == 1:
                    q.append((nx, ny))
                    info[nx][ny] = info[x][y] + 1

bfs(0, 0)
print(info[n-1][m-1]-1)


