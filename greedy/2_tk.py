N, M, K = map(int, input().split())
nums = []
nums = list(map(int, input().split()))
nums = sorted(nums)
biggest = nums[-1]
second = nums[-2]
result = 0
while M > 0:
  if M >= K + 1:
    result = result + biggest*K + second
    M = M - (K + 1)
  else:
    result = result + biggest*K
    M = M - K
    break
print(result)

# M >= K+1 면 biggest*K+second+1
# M < K + 1이면 bigeest*K