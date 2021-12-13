# 2

n = int(input())
nums = [int(input()) for _ in range(n)]
for i in reversed(sorted(nums)):
  print(i, end=' ')

# 3

n = int(input())

people = {}

for _ in range(n):
  name, score = input().split()
  people[name] = int(score)

for i,_ in sorted(people.items(), key=lambda x:x[1]):
  print(i, end=' ')

# 4

n, k = map(int, input().split())
a = sorted(list(map(int, input().split())))
b = sorted(list(map(int, input().split())), reverse=True)

result = sum(a)
for x, y in zip(a[0:0+k], b[0:0+k]):
  if x >= y:
    break
  result += y - x
print(result)