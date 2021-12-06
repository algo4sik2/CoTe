# 상하좌우
n = int(input())
x, y = 1,1
plans = input().split()

# L, R, U, D에 따른 이동 방향
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

for plan in plans:
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
        if nx < 1 or ny < 1 or nx > n or ny > n:
            continue

        x, y = nx, ny

print(x, y)


# 시각
n = int(input())
count = 0

for i in range(n+1):
    for j in range(60):
        for k in range(60):
            if (i%10==3) or (j//10==3) or (j%10==3) or (k//10==3) or (k%10==3):
                count += 1


print(count)


# 왕실의 나이트
n = list(input())

count = 0
x = ord(n[0])-96
y = int(n[1])

dx = [2, 2, -2, -2, 1, 1, -1, -1]
dy = [1, -1, 1, -1, 2, -2, 2, -2]

for i in range(len(dx)):
    nx = x + dx[i]
    ny = y + dy[i]
    
    if nx < 1 or nx > 8 or ny < 1 or ny > 8:
        continue

    count += 1

print(count)

# 왕실의 나이트
n = list(input())

count = 0
x = ord(n[0])-96
y = int(n[1])

dx = [2, 2, -2, -2, 1, 1, -1, -1]
dy = [1, -1, 1, -1, 2, -2, 2, -2]

for i in range(len(dx)):
    nx = x + dx[i]
    ny = y + dy[i]
    
    if nx < 1 or nx > 8 or ny < 1 or ny > 8:
        continue

    count += 1

print(count)

# 게임 개발
# 전 왜 안될까요...?? 뭐가 틀린걸까요ㅠㅠㅠ
n, m = map(int, input().split()) # n X m 맵

x, y, d = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]
chk = [[0]*m for _ in range(n)] # 안 가본 곳 0으로 초기화

chk [x][y] = 1

dx = [-1, 0, 1, 0]  # 북, 동, 남 서 방향의 x좌표
dy = [0, 1, 0, -1]

count = 1
ch = 0 # 방향 다 돌았는지 체크

while True:
    if d == -1:
        d == 3
    else:
        d -= 1

    nx = x+dx[d]
    ny = y+dy[d]

    # 방향을 돌고 앞 쪽의 타일이 한번도 안 가본 육지인 경우
    if (arr[nx][ny]==0) & (chk[nx][ny]==0):
        x, y = nx, ny
        chk[x][y] = 1
        ch = 0
        count += 1
        continue

    else:
        ch += 1
        # 방향 다 돌았을 때
        if ch == 4:
            nx = x-dx[d]
            ny = y-dy[d]

            if arr[nx][ny] == 0:
                x, y = nx, ny
            else:
                break
            ch = 0

print(count)

# 럭키 스트레이트
n = int(input())

list = []
result = 0
while True:
    tmp = n%10
    list.append(tmp)
    n = n//10

    if n < 10:
        list.append(n)
        break

for i in range(len(list)):
    if i < len(list)//2:
        result += list[i]

    else:
        result -= list[i]


if result == 0:
    print("LUCKY")

else:
    print("READY")

# 문자열 재정렬
n = input()
alpha = []
num = []

for i in range(len(n)):
    if n[i].isalpha()==1:
        alpha.append(n[i])
    else:
        num.append(n[i])

alpha.sort()
num.sort()

result = alpha + num

print(''.join(result))