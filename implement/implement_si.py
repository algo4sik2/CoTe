import sys
sys.stdin = open("input.txt", "r")

# 예제 4-1 상하좌우(p.110)
n = int(input())
info = list(input().split())
x, y = 1, 1

for ch in info:
    temp_x, temp_y = x, y
    if ch == 'R':   temp_x += 1
    elif ch == 'L': temp_x -= 1
    elif ch == 'U': temp_y -= 1
    elif ch == 'D': temp_y += 1
    if 0 < temp_x <= n and 0 < temp_y <= n:
        x, y = temp_x, temp_y

print(y, x)

#-----------------------------------------#

# 예제 4-2 시각(p.113)
n = int(input())
cnt = 0
for h in range(n+1):
    for m in range(60):
        for s in range(60):
            if '3' in str(h)+str(m)+str(s):
                cnt += 1
print(cnt)

#-----------------------------------------#

# 실전문제 왕실의 나이트(p.115)
pos = input()
x, y = ord(pos[0])-ord('a'), int(pos[1])-1

dx = [1, 2, 2, 1, -1, -2, -2, -1]
dy = [2, 1, -1, -2, -2, -1, 1, 2]

cnt = 0
for i in range(8):
    nx = x + dx[i]
    ny = y + dy[i]
    if 0 <= nx < 8 and 0 <= ny < 8:
        cnt += 1
print(cnt)

#-----------------------------------------#

# 실전문제 게임 개발(p.118)
n, m = map(int, input().split())
y, x, d = map(int, input().split())
info = []
for _ in range(n):
    info.append(list(map(int, input().split())))

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
cnt = 0
while True:
    Flag = False
    for i in range(4):
        d = d - 1 if d - 1 >= 0 else 3
        nx = x + dx[d]
        ny = y + dy[d]
        if info[ny][nx] != 1:
            if info[ny][nx] != 2:
                info[ny][nx] = 2
                x, y = nx, ny
                Flag = True
                cnt += 1
                break
    if Flag == False:
        nx = x - dx[d]
        ny = y - dy[d]
        if info[ny][nx] != 1:
            x, y = nx, ny
        else:
            break
print(cnt)

#-----------------------------------------#

# 럭키 스트레이트(p.321)
n = input()
mid = len(n)//2
left, right = n[:mid], n[mid:]
left_sum, right_sum = 0, 0
for num in left:    left_sum += int(num)
for num in right:   right_sum += int(num)
if left_sum == right_sum:
    print("LUCKY")
else:
    print("READY")

#-----------------------------------------#

# 문자열 재정렬(p.322)
s = list(input())
s.sort()
result, sum = [], 0
for num in s:
    if '0' <= num <= '9': sum += int(num)
    else: result.append(num)
result.append(str(sum))
print("".join(result))


