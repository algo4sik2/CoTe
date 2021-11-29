# 거스름돈
n = 1260
count = 0

list = [500, 100, 50, 10]

for i in list:
    count += n // i
    n %= i

print(count)