# 4-1 상하좌우

n = int(input())

x,y = 1,1
plans = input().split()
dx = [0,0,-1,1]
dy = [-1,1,0,0]
move_types = ['L','R','U','D']

for plan in plans:
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x+dx[i]
            ny = y+dy[i]

    if nx < 1 or ny <1 or nx > n or ny >n:
        continue

    x,y = nx,ny

print(x,y)

#4-2 시각 경우의수
time = int(input())

count = 0
for i in range(time+1):
    for j in range(60):
        for b in range(60):
            if '3' in str(i) + str(j) + str(b):
                count += 1

print(count)

#실전문제 2 왕실의 나이트

location = input()
row = int(location[1])
column = int(ord(location[0])) - int(ord('a'))+1

steps = [(-2,-1),(-1,-2),(1,-2),(2,-1),(2,1),(1,2),(-1,2),(-2,1)]

result = 0
for step in steps:
    next_row = row + step[0]
    next_column = column + step[1]

    if next_row >= 1 and next_row <=8 and next_column >= 1 and next_column <= 8:
        result += 1

print(result)

# 실전문제 3 게임 개발
n,m = map(int, input().split())

d = [[0] * m for _ in range(n)]

x,y,posit=map(int, input().split())
d[x][y] = 1

array = []
for i in range(n):
    array.append(list(map(int, input().split())))
dx = [-1,0,1,0]
dy = [0,1,0,-1]
def turn_left():
    global posit
    posit -= 1
    if posit == -1:
        posit = 3
count = 1
turn_time = 0

while True:
    turn_left()
    nx = x + dx[posit]
    ny = y + dy[posit]

    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    else:
        turn_time +=1

    if turn_time == 4:
        nx = x - dx[posit]
        ny = y - dy[posit]

        if array[nx][ny] ==0:
            x = nx
            y = ny
        else:
            break
        turn_time = 0

print(count)