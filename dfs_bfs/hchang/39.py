# 순환구조가 없는지 확인하라
# [[1,0],[0,1]] 이렇게 있으면 순환!
n, schedule = 4, [[1,3],[5,3],[0,5],[3,0],[5,1]]

# idea: 그래프 구조로 바꾸었을 때, 서로 상대방을 가진 인자가 없으면 된다. -> 땡
# 그 다음: 각각 위치에서 시작한 후, 이미 지나간 수가 나오지 않으면 된다. -> 좋을 듯?
from collections import defaultdict

numtree = defaultdict(set)
start_list = set()
for i in schedule:
    numtree[i[0]].add(i[1])
    start_list |= set(i)


def dfs(start_n,discover):
    if start_n in discover:
        return False, discover
    discover.add(start_n)
    for i in numtree[start_n]:
        return dfs(i, discover)
    return True, discover
    
bol = True
print(numtree)
print(start_list)

while start_list:
    discover = set()
    start_n = start_list.pop()
    bol, discovered = dfs(start_n,discover)
    if not bol:
        print("순환!", discovered, start_n)
        break
    start_list -= discovered
if bol: print("순환 없음!")


        


