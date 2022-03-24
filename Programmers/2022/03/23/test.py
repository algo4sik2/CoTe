
info, query, answer = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"], \
    ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"],[1,1,1,1,2,4]




def solution(info, query):
    answer = []
    query_dict = {}
    for i in query:
        ...
    for i in query:
        i = i.split(' and ')
        i = i[:-1] + i[-1].split()
        count = 0
        for j in info:
            j = j.split()
            check = True
            for a,b in zip(i[:-1],j[:-1]):
                if a!=b and a!='-':
                    check=False
                    break
            if check and int(i[-1]) <= int(j[-1]):
                count += 1
        answer.append(count)

    return answer

result = solution(info, query)

print(answer, result)
if answer==result: print('정답')
else: print('땡!')