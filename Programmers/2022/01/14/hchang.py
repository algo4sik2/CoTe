
def compress(s, leng):
    lst = []
    eli = ''
    count = 0
    
    for i in s:
        count += 1
        eli += i
        if count==leng:
            lst.append(eli)
            count = 0
            eli = ''
        
    anslst = [1,lst[0]]
    for i in lst[1:]:
        if i == anslst[-1]:
            anslst[-2] += 1
        else:
            anslst += [1,i]
    if len(eli) > 0:
        anslst += [eli]
    
    answer = []
    for i in anslst:
        if i != 1:answer.append(str(i))
    answer = ''.join(answer)
    return answer



def solution(s):
    N = len(s)
    anslst = []
    for i in range(1,(N//2)+2):
        ans = compress(s,i)
        anslst.append((len(ans),ans))
    answer, _ = sorted(anslst, reverse=True).pop()
    print(_)
    return answer
                   
