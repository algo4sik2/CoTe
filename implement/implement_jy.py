# 4-1) 상하좌우

n = int(input())
x, y = 1, 1

a = list(input().split())

for i in range(len(a)):
    if a[i] == 'L':
        if y != 1:
            y -= 1
        else:
            y = y
    
    if a[i] == 'R':
        if y != n:
            y += 1
        else:
            y = y
    
    if a[i] == 'U':
        if x != 1:
            x -= 1
        else:
            x = x
            
    if a[i] == 'D':
        if x != n:
            x += 1
        else:
            x = x
      
print(x, y)

#------------------------------------------------------
# 4-2) 시각

n = int(input())
cnt = 0

for i in range(0, n+1):
    for j in range(0, 60):
        for k in range(0, 60):
            if '3' in str(i) + str(j) + str(k):
                cnt += 1
                
print(cnt)

#------------------------------------------------------
# 실전 문제 ) 왕실의 나이트

dx = [2, 2, -2, 2, 1, -1, 1, -1]
dy = [1, -1, 1, -1, 2, 2, -2, -2]

a = input()

cnt = 0

for i in range(8):
    
    row = int(a[1])
    col = int(ord(a[0])) - int(ord('a')) + 1
    row += dx[i]
    col += dy[i]
    
    if row >= 1 and row <= 8 and col >= 1 and col <= 8:
        cnt += 1
        
print(cnt)

#------------------------------------------------------
# 실전 문제 ) 게임 개발

#------------------------------------------------------
# 07 ) 럭키 스트레이트

n = input()

first_sum = 0
last_sum = 0


for i in range((len(n)//2)):
    first_sum += int(n[i])

for i in range((len(n)//2), len(n)):
    last_sum += int(n[i])
    
if (first_sum == last_sum):
    print('LUCkY')
else:
    print('READY')
    
#------------------------------------------------------
# 08 ) 문자열 재정렬

n = input()

alphabets = []
nums = []
sum = 0

for i in range(len(n)):
    if (n[i] == '0' or n[i] == '1' or n[i] == '2' or n[i] == '3' or n[i] == '4' or n[i] == '5' or n[i] == '6' or n[i] == '7' or n[i] == '8' or n[i] == '9'):
        nums.append(int(n[i]))
    else:
        alphabets.append(n[i])

alphabets.sort()        
for a in alphabets:
    print(a, end='')

for num in nums:
    sum += num
    
print(sum)


