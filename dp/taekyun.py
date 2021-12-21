# 2

n = int(input())
dp = [0] * (n + 1)
for i in range(2, n + 1):
    dp[i] = dp[i - 1] + 1
    if i % 5 == 0:
        print(i, dp)
        print(dp[i // 5], dp[i - 1])
        dp[i] = min(dp[i // 5], dp[i - 1]) + 1
        print(i, dp)
    if i % 3 == 0:
        dp[i] = min(dp[i // 3], dp[i - 1]) + 1        
    if i % 2 == 0:
        dp[i] = min(dp[i // 2], dp[i - 1]) + 1

print(dp[n])

# 3
# a_2 = a_2 + a_0, a_new = a + max(a_n-2 + a_n-3)

n = int(input())
l = list(map(int, input().split()))

l[2] += l[0]
for i in range(3, n):
    l[i] += max(l[i - 2], l[i - 3])
print(max(l[n - 1], l[n - 2]))