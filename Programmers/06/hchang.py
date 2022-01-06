
num = ['0','1']
numlist = []



def solution(n, arr1, arr2):
    def dfs(n,eliment=''):
        if len(eliment)==n:
            numlist.append(eliment)
            return
        for i in num:
            eliment += i
            dfs(n,eliment)
            eliment = eliment[:-1]

    dfs(n)
    now = [[' ']*n for i in range(n)]
    real = []
    for i,j in enumerate(arr1):
        for k, l in enumerate(numlist[j]):
            if l == '1':
                now[i][k] = '#'
        
    for i,j in enumerate(arr2):
        for k, l in enumerate(numlist[j]):
            if l == '1':
                now[i][k] = '#'
    
    for i in now:
        a = ''.join(i)
        real.append(a)
    answer = real
    return answer
