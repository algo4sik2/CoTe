# (실전 문제) 큰 수의 법칙

n, m, k = input('n, m, k 입력 : ').split()
n, m, k = int(n), int(m), int(k)


ls = list(map(int, input().split()))


cnt = 0
sum = 0    

for i in range(len(ls)):
    for j in range(i):
        if ls[j] < ls[i]:
            ls[i], ls[j] = ls[j], ls[i]

for _ in range(m):
    if cnt == k:
        sum += ls[1]
        cnt = 0
    else:
        sum += ls[0]
        cnt += 1
        
print(sum)