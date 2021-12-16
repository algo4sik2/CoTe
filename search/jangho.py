# bupum


def binary_search(arr, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if n_list[mid] == target:
            return target
        elif n_list[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None


N = int(input())
n_list = list(map(int, input().split()))

M = int(input())
m_list = list(map(int, input().split()))

n_list.sort()

for i in m_list:
    result = binary_search(n_list, i, 0, N - 1)
    if result != None:
        print("yes", end=" ")
    else:
        print("no", end=" ")


#####################################################################
# dduck


def binary_search(arr, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if n_list[mid] == target:
            return target
        elif n_list[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None


N = int(input())
n_list = list(map(int, input().split()))

M = int(input())
m_list = list(map(int, input().split()))

n_list.sort()

for i in m_list:
    result = binary_search(n_list, i, 0, N - 1)
    if result != None:
        print("yes", end=" ")
    else:
        print("no", end=" ")
