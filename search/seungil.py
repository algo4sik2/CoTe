# 실전문제 2 부품찾기(p.197)
n = int(input())
arr = list(map(int, input().split()))
m = int(input())
req = list(map(int, input().split()))

# 풀이 1
for i in req:
    if i in arr:
        print('yes', end=' ')
    else:
        print('no', end=' ')

# 풀이 2
def search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return search(array, target, start, mid-1)
    else:
        return search(array, target, mid+1, end)

for i in req:
    result = search(arr, i, 0, n-1)
    if result != None:
        print('yes', end=' ')
    else:
        print('no', end=' ')

#----------------------------------------------#

# 실전문제 3 떡볶이 떡 만들기(p.201)
n, m = map(int, input().split())
arr = list(map(int, input().split()))

max_h = max(arr)

def search(array, target, start, end):
    add = 0
    if start > end:
        return None

    mid = (start + end) // 2

    for i in arr:
        if i > mid:
            add += i - mid

    if add == target:
        return mid
    elif add < target:
        return search(array, target, start, mid-1)
    else:
        return search(array, target, mid+1, end)

result = search(arr, m, 1, max_h-1)
print(result)


