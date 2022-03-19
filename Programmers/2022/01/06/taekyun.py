def solution(n, arr1, arr2):
    c = [' ', '#']
    answer = []
    for i,j in zip(arr1, arr2):
        arr = ''
        num = i | j
        for _ in range(n):
            arr = c[num % 2] + arr
            num = num // 2
        answer.append(arr)
    return answer