from time import time

info, query, answer = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"], \
    ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"],[1,1,1,1,2,4]


# from collections import defaultdict
# from functools import reduce

# def setsum(setlist) -> set:
#     return reduce(lambda x,y: x | y, setlist, set())

# def solution(info, query):
#     answer = []
#     db = defaultdict(set)
#     query_dict = dict()
#     for n, inf in enumerate(info):
#         inf = inf.split()
#         score = inf.pop()
#         for f in inf:
#             db[f].add((score,n))
#     for q in query:
#         q = q.split()
#         q_list = [i for i in q if i != 'and' and i!= '-']
#         score = q_list.pop()
#         q_string = ''.join(q_list)
#         if q_string in query_dict:
#             q_num = query_dict[q_string]
#         else:
#             if q_list:
#                 q_num = db[q_list.pop()].copy()
#                 for i in q_list:
#                     q_num &= db[i]
#             else: q_num = setsum(db.values())
#             query_dict[q_string]=q_num #sorted(q_num)
#         q_num = [i for i in q_num if int(i[0]) >= int(score)]
#         answer.append(len(q_num))
#     return answer

from collections import defaultdict
from functools import reduce

def setsum(setlist) -> set:
    return reduce(lambda x,y: x | y, setlist, set())

# def bisearch_l(lst: list, find_num: int) -> int:
#     start = 0
#     end = len(lst) - 1
#     index = (start + end)//2

#     while start < end:
#         if lst[index][0]<find_num:
#             start = index + 1
#         elif lst[index][0]>=find_num:
#             end = index
#         index = (start + end)//2
#     return index
def bisearch_r(lst: list, find_num: int) -> int:
    start = 0
    end = len(lst) - 1
    index = (start + end)//2
    
    while start < end:
        if lst[index][0]<=find_num:
            start = index
        elif lst[index][0]>find_num:
            end = index-1
        index = (start + end + 1)//2
    return index


def solution(info, query):
    answer = []
    db = defaultdict(set)
    query_dict = dict()
    for n, inf in enumerate(info):
        inf = inf.split()
        score = inf.pop()
        for f in inf:
            db[f].add((int(score),n))
    
    for q in query:
        q = q.split()
        q_list = [i for i in q if i != 'and' and i!= '-']
        score = q_list.pop()
        q_string = ''.join(q_list) # javajunierpizza
        if q_string in query_dict:
            q_num = query_dict[q_string]
        else:
            if q_list:
                q_num = db[q_list.pop()].copy()
                for i in q_list:
                    q_num &= db[i] # {1,2,3} & {2,3,4} = {2,3} ->  |  = {1,2,3,4}
            else: q_num = setsum(db.values())
            q_num = sorted(q_num)
            query_dict[q_string]=q_num
        score = int(score)

        answer.append(bisearch_r(q_num,score))
    return answer

# def solution(info, query):
#     answer = []
#     for i in query:
#         i = i.split(' and ')
#         i = i[:-1] + i[-1].split()
#         count = 0
#         for j in info:
#             j = j.split()
#             check = True
#             for a,b in zip(i[:-1],j[:-1]):
#                 if a!=b and a!='-':
#                     check=False
#                     break
#             if check and int(i[-1]) <= int(j[-1]):
#                 count += 1
#         answer.append(count)
#     return answer

st = time()
result = solution(info, query)
print(f'????????????: {time() - st}')
print(answer, result)
if answer==result: print('??????')
else: print('???!')