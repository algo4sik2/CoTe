from functools import reduce
from collections import Counter

def solution(id_list, report, k):
    answer = [0 for _ in range(len(id_list))]
    users = {i:[] for i in id_list}
    for r in report:
        er, ee = r.split(' ')
        if ee not in users[er]:
            users[er] += [ee]
    total = list(reduce(lambda x,y:x+y, users.values()))
    for key, v in Counter(total).items():
        if v >= k:
            for i, val in enumerate(users.values()):
                if key in val:
                    answer[i] += 1
    return answer