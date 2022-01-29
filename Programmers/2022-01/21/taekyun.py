answer = 0

def dfs(dest, dest_len, n, total, sign, target):
    if sign == '+':
        total += dest[n]
    elif sign == '-':
        total -= dest[n]
    n = n + 1
    if n == dest_len:
        if total == target:
            global answer
            answer += 1
        return
    dfs(dest, dest_len, n, total, '+', target)
    dfs(dest, dest_len, n, total, '-', target)
    
    
def solution(numbers, target):
    dest_len = len(numbers)
    dfs(numbers, dest_len, 0, 0, '+', target)
    dfs(numbers, dest_len, 0, 0, '-', target)
    return answer