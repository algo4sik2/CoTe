L = [1,4,7,'*']
R = [3,6,9,'#']
M = [2,5,8,0]

def solution(numbers, hand):
    answer = ''
    left_now = "*"
    right_now = "#"
    for i in numbers:    
        if i in L:
            answer += 'L'
            left_now = i
            continue
        if i in R:
            answer += 'R'
            right_now = i
            continue
        # 가운데는 거리를 계산한다.
        # print(i)
        # print(left_now)
        # print(right_now)
        m = M.index(i)
        if left_now in L:
            dl = abs(L.index(left_now) - m) + 1
        else: dl = abs(M.index(left_now) -m)
        if right_now in R:
            dr = abs(R.index(right_now) - m) + 1
        else: dr = abs(M.index(right_now) - m)
            
        if dl > dr:
            answer +="R"
            right_now = i
        elif dl < dr:
            answer +="L"
            left_now = i
        elif hand == 'right':
            answer += "R"
            right_now = i
        else:
            answer +="L"
            left_now = i
            
    return answer
