# 위에서 아래로

n = int(input())
nums = []
for i in range(n):
    nums.append(int(input()))
    
# 1. library

nums.sort(reverse=False)
print(nums)



# 2. implement

for i in range(len(nums)):
    for j in range(i):
        if nums[j] < nums[i]:
            nums[j], nums[i] = nums[i], nums[j]
            
print(nums)
    
