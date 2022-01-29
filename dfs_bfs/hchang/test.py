_input = "236"

alpa = [0,0,"abc", "def","ghi","jkl","mno","pqrs","tuv","wxyz"]
#--------------
answer = []
eliment = []

def dfs(num):
    if num==len(_input):
        answer.append(''.join(eliment))
        return
    for i in alpa[int(_input[num])]:
        eliment.append(i)
        dfs(num+1)
        eliment.pop()

dfs(0) # dfs(1) -> dfs(2) [a,e] -> dfs(3) 
print(answer)
