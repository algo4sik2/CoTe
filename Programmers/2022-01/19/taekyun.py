def solution(n):
    answer = ''
    base = ['1','2','4']
    while n > 0:
        n = n - 1
        answer = base[n % 3] + answer
        n = n // 3
    return answer