def solution(s):
    result = []
    for i in range(1, (len(s)//2) + 1):
        cnt = 0
        tmp = ""
        for j in range(0, len(s), i):
            if s[j:j+i] == s[j+i:j+i+i]:
                cnt += 1
            else:
                if cnt > 0:
                    tmp = tmp + str(cnt+1) + s[j:j+i]
                    cnt = 0
                else:
                    tmp += s[j:j+i]
        result.append(tmp)
    
    minimum = len(s)
    for i in result:
        if len(i) < minimum:
            minimum = len(i)
    
    answer = minimum
    return answer