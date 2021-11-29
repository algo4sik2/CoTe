# 숫자 카드 게임

n, m = map(int, input().split())
result = 0

for i in range(n):
    data = list(map(int, input().split()))
    data.sort()
    min = data[0]
    # min_data = min(data)
    result = max(min, result)

print(result)