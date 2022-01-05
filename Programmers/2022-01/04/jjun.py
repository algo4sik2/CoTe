def solution(N, stages):
    answer = []
    my_dict = {}
    i = 1
    total = 0
    fail = 0
    while (i <= N):
        for stage in stages:
            if stage >= i:
                total += 1
                if stage == i:
                    fail += 1
        if total == 0:
            ratio = 0
        else:
            ratio = fail / total
        my_dict[i] = ratio
        fail, total = 0, 0
        i += 1
    
    sort = sorted(my_dict.items(), reverse=True, key=lambda item:item[1])
    for key,_ in sort:
        answer.append(key)
        
    return answer