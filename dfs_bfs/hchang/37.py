#
# 모든 부분 집합을 만들어라

# nums = [1,2,3]


# answer = []
# eliment = []



# def dfs(num=0):
#     answer.append(eliment[:])

#     for i, j in enumerate(nums[num:]):
#         eliment.append(j)
#         dfs(num+i+1)
#         eliment.pop()
# dfs()

# print(answer)

nums = [1,2,3]
answer = []
eliment = []

def dfs(n):
    answer.append(eliment[:])

    for i in nums[n:]:
        eliment.append(i)
        n += 1
        dfs(n)
        eliment.pop()

dfs(0)
print(answer)
