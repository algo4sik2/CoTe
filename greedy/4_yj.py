# 1이 될 때까지

n, k = map(int, input().split())
count = 0

while n!=1:
    if n%k==0:
        n = n//k
        count += 1
    else:
        count += (n%k)
        n -= (n%k)

print(count)