from collections import deque

q = deque()

def solution(progresses, speeds):
    answer = []
    days = 0
    index = 0
    for i in progresses:
        q.append(i)

    while q:
        a = q.popleft()
        if a + days*speeds[index] < 100:
            if (100-a-days*speeds[index]) % speeds[index] == 0:
                d = (100-a-days*speeds[index]) // speeds[index]
                days += d
                answer.append(1)
            else:
                d = (100-a-days*speeds[index]) // speeds[index]
                days = days + d + 1
                answer.append(1)                            
        else:
            answer[-1] += 1              
        index += 1
        
    return answer
