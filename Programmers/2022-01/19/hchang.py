# num = ['1','2','4']
# result = []
# def dfs(N, eliments = []):
#     if len(eliments)==N:
#         result.append(''.join(eliments))
#         return
#     for i in num:
#         eliments.append(i)
#         dfs(N, eliments)
#         eliments.pop()

def solution(n):
    count = 0
    answer = ''
    for i in range(n):
        count += 1
        if n > 3**count:
            n -= 3**count
        else: break
    # dfs(count)
    answer = ''
    for i in range(count,0,-1):
        if n > (3**(i-1))*2:
            answer += '4'
            n -= (3**(i-1))*2
        elif n > 3**(i-1):
            answer += '2'
            n -= 3**(i-1)
        else: answer += '1'
    return answer
