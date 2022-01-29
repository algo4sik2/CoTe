def solution(id_list, report, k):
    length = len(id_list)
    user = {x : 0 for x in id_list}
    answer = [0 for i in range(length)]
    
    # 신고 당한 유저의 신고 수 1씩 증가
    for i in set(report):
        user[i.split()[1]] += 1
        
    # k 보다 신고 많이 받았으면, 신고한 사람의 결과 1 증가
    for i in set(report):
        if user[i.split()[1]] >= k:
            answer[id_list.index(i.split()[0])] += 1
            
    return answer
