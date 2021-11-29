# (실전 문제) 1이 될 때까지

n, k = map(int, input().split())
cnt = 0

while n != 1:
    
    while n % k != 0:
        n -= 1
        cnt += 1
        
    n = n // k
    cnt += 1
    
print(cnt)
    
