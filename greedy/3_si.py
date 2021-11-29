n, m = map(int, input().split())
data = [0]*m
result = 0
for i in range(n):
    data[i] = list(map(int, input().split()))
    temp = min(data[i])
    result = max(result, temp)
print(result)

