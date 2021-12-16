# 부품 찾기

# 이진 탐색 소스코드 구현(재귀 함수)
def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) //2
    # 찾은 경우 중간점 인덱스 반환
    if array[mid] == target:
        return mid
    # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
    elif array[mid] > target:
        return binary_search(array, target, start, mid -1)
    # 중간점의 값보다 찾고자 하는 값이 작은 경우 오른쪽 확인
    else:
        return binary_search(array, target, mid+1, end)

# 전체 원소 입력받기
m = int(input())
array = list(map(int, input().split()))
array.sort()
# n(찾고자 하는 원소의 개수)과 target(찾고자 하는 문자열)을 입력받기
n = int(input())
target = list(map(int, input().split()))

for i in range(n):    
    # 이진 탐색 수행 결과 출력
    result = binary_search(array, target[i], 0, m-1)
    if result == None:
        print("no", end = ' ')
    else:
        print("yes", end = ' ')

print('\n')

# ------------------------------------------------ #

# 떡볶이 떡 만들기

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        # print(mid)

        result = 0   
        for i in array:
            if i>mid:
                temp = i-mid
                result += temp

        # print(result)

        # 찾은 경우 중간점 인덱스 반환
        if result == target:
            return mid

        elif result < target:
            end = mid -1

        else:
            start = mid + 1

    return mid-1

# n은 떡의 갯수 m은 요청한 떡의 길이
n, m = map(int, input().split())
array = list(map(int, input().split()))

x = binary_search(array, m, 0, max(array))
print(x)