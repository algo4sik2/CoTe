""" 
### **문제 설명**

`n`개의 노드로 이루어진 트리가 있습니다. 각 노드에는 0번부터 `n-1`번까지 번호가 매겨져 있습니다. 
이때, 당신은 다음 조건을 모두 만족하는 정수 순서쌍 `(i,j,k)`의 개수를 구하고자 합니다.

- 0 ≤ `i`, `j`, `k` < `n`
- `i`, `j`, `k`는 서로 다릅니다.
- `distance(a, b)`를 `a`번 노드와 `b`번 노드를 잇는 경로 상의 간선의 개수라고 할 때, 
`distance(i, j) + distance(j, k) = distance(i, k)`입니다.

트리의 노드 개수를 의미하는 `n`과 간선 정보가 담긴 2차원 정수 배열 `edges`가 매개변수로 주어집니다. 
주어진 조건을 모두 만족하는 순서쌍 `(i,j,k)`의 개수를 return 하도록 solution 함수를 완성해주세요.

---
[0,1], [0,2], [1,3]

-1
0                         -2
1            2             99
3 4 5        6 7 8
9            

3,6,9
3,6 -> 0 
6,9 -> 0  --> 조건 만족
3,9 -> 3  --> 조건 만족

3,6 -> 3  --> 조건 만족 
6,9 -> 
3,9 ->

---

### 제한사항

- 3 ≤ `n` ≤ 300,000
- `edges`의 행의 개수 = `n` - 1
- `edges`의 각 행은 `[v1,v2]` 2개의 정수로 이루어져 있으며, 이는 `v1`번 노드와 `v2`번 노드 사이에 간선이 있음을 의미합니다.
    - `0 ≤ v1 < n`
    - `0 ≤ v2 < n`
    - `v1 ≠ v2`
    - `edges`가 의미하는 그래프가 항상 트리인 경우만 입력으로 주어집니다.

---

### 입출력 예 
n   edges                       result
5	[[0,1],[0,2],[1,3],[1,4]]	16
4	[[2,3],[0,1],[1,2]]	        8
### 입출력 예 설명

**입출력 예 #1**

- 다음 그림은 입력으로 주어진 트리를 나타낸 것입니다.

![https://grepp-programmers.s3.ap-northeast-2.amazonaws.com/files/production/f16dc144-6770-4a69-8f1b-7a8ad1b0bb81/ex1.png](https://grepp-programmers.s3.ap-northeast-2.amazonaws.com/files/production/f16dc144-6770-4a69-8f1b-7a8ad1b0bb81/ex1.png)

# """
nlist = [5]#,4]
edgeslist = [[[0,1],[0,2],[1,3],[1,4]]]#,\
             #[[2,3],[0,1],[1,2]]]
# 0-1-3-4
#  -2
from itertools import permutations

def aligncheck(nodes, tree) -> bool:
    a,b,c = nodes
    aroot = []
    croot = []
    olda, oldc = a,c
    while type(a)==int:
        aroot.append(tree[a])
        a = tree[a]
    while type(c)==int:
        croot.append(tree[c])
        c = tree[c]
    
    if (b in croot or b in aroot) and not olda in croot and not oldc in aroot :
        return True
    elif:
        return
    else: return False
    




def solutions(n, edges):
    answer = 0
    tree = [None for _ in range(n)]
    
    for i, j in edges:
        tree[j] = i
    
    for i in permutations(range(n), 3):
        print(i) # 나가세용ㅋㅋ
        print(aligncheck(i, tree))
        answer += aligncheck(i, tree)

    return answer





count = 1 
for i, j in zip(nlist, edgeslist):
    print(f"{count}번 정답:")
    print(solutions(i,j))
    count += 1

