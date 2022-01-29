# 일정 재구성
# [from, to]로 구성된 항공권 목록
# JFK에서 출발하는 여행일정을 완성하라

# ticket = [['MUC','LHR'],['JFK','MUC'],['SFO', 'SJC'],['LHR','SFO']]
ticket = [[ "JFK" , "SFO" ] , [ "JFK" , "ATL" ] , [ "SFO" , "ATL" ] , [ "ATL" , "JFK" ] , [ "ATL" , "SFO" ] ]
ticket.sort(reverse=True)

def from2go_list(frm):
    go = [i[1] for i in ticket if i[0]==frm]
    if go:
        return go

go_list = {}

for i in ticket:
    go_list[i[0]] = from2go_list(i[0])


answer = []
a = 'JFK'
for i in range(len(ticket)):
    answer.append(a)
    a = go_list[a].pop()
answer.append(a)

print(answer)

# from collections import defaultdict

# graph = defaultdict(list)
# print(graph)