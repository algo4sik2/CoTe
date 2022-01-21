# 타겟 넘버

def solution(numbers, target):
    answer = 0
    num = len(numbers)
    
    def solve(x, y):   
        if x == num:
            if y == target:
                nonlocal answer
                answer += 1
                return
        
        else:
            solve(x+1, y+1*numbers[x])
            solve(x+1, y-1*numbers[x])
        
    solve(0,0)    
    return answer
  
 # 문제 오류 원인
 # 1. index 벗어난다고 오류 -> 원래 num = len(numbers)-1 이라고 했다. 고치니깐 해결! 
 # 2. answer에서 오류 -> nonlocal answer처리해서 전역변수를 가져옴
 # 교훈 : 차근차근 (0,0)을 넣었을 때 어떻게 되는지 생각하자!!!
