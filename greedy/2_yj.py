# 큰 수의 법칙

n, m, k = input().split()
n = int(n)
m = int(m)
k = int(k)

a = input().split()
a = list(map(int, a))

max = 0
s = m // (k+1)  # 두번재로 큰 수 더하는 횟수 구하는 식

for i in range(n):
    for j in range(i+1, n): # 제일 큰 수가 a[i], 두번째 큰 수가 a[j]라고 가정
        sum = a[i]*(m-s) + a[j]*s
        sum2 = a[j]*(m-s) + a[i]*s
        if max<sum:
            max = sum
        if max<sum2:
            max = sum2
        
print(max)

