n, m, k = map(int, input().split())
data = list(map(int, input().split()))
data.sort()

first, second = data[n-1], data[n-2]
result = 0

count = (m/(k+1)) * k
count += m%(k+1)

result = count * first
result += (m-count)*second


