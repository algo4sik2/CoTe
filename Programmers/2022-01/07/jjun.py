def solution(dartResult):
    
    hit = []
    answer = 0
    
    for i in range(len(dartResult)):
        if dartResult[i].isdigit():
            if dartResult[i] == '0' and i == 0:
                hit.append(int(dartResult[i]))
            elif(dartResult[i] == '0' and dartResult[i-1] == '1'):
                pass
            elif dartResult[i+1].isdigit():
                hit.append(int(dartResult[i] + dartResult[i+1]))
            else:
                hit.append(int(dartResult[i]))
                        
        if dartResult[i].isalpha():
            if dartResult[i] == 'S':
                pass
            elif dartResult[i] == 'D':
                hit[-1] = hit[-1] ** 2
            else:
                hit[-1] = hit[-1] ** 3
        
        else:
            if dartResult[i] == '*':
                if len(hit) < 2:
                    hit[-1] = hit[-1] * 2
                else:
                    hit[-2] = hit[-2] * 2
                    hit[-1] = hit[-1] * 2
            if dartResult[i] == '#':
                hit[-1] = hit[-1] * (-1)
                
    for i in hit: 
        answer += i
            
    return answer