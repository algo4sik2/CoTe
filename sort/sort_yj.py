# 위에서 아래로
n = int(input())
arr = []

for i in range(n):
    arr.append(int(input()))

for i in range(len(arr)):
    min_index = i
    for j in range(i + 1, len(arr)):
        if arr[min_index] < arr[j]:
            min_index = j
    arr[i], arr[min_index] = arr[min_index], arr[i]

print(arr)

#-------------------------------------------#

# 성적이 낮은 순서로 학생 출력하기
n = int(input())
arr = []

for i in range(n):
    s1, s2 = input().split()
    arr.append([s1, int(s2)])

arr = sorted(arr, key=lambda arr: arr[1])

for i in range(n):
    print(arr[i][0], end= ' ')

# def setting(data):
#     return data[1]

# def res(data):
#     for i in range(len(data)):
#         print(data[i][0], end = ' ')

# result = sorted(arr, key = setting, reverse = False)

# res(result)
# print('\n')

#-------------------------------------------#

# 두 배열의 원소 교체
n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

sum = 0
a = sorted(a)
b = sorted(b, reverse=True)

for i in range(n):
    if i < k and a[i] < b[i]:
        sum+=b[i]
    else:
        sum+=a[i]

print(sum)   
