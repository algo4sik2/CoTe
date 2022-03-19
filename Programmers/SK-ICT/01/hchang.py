""" 문제 설명
6종류(1원, 5원, 10원, 50원, 100원, 500원)의 동전을 생산하는 공장이 있습니다. 특정 금액만큼 동전을 생산해달라는 의뢰가 들어왔을 때, 최소 비용으로 그 금액만큼 동전을 생산하고자 합니다.

화폐 단위(원)   생산 단가(원)
1   1
5   4
10   99
50   35
100   50
500   1000
만약 각 동전의 생산 단가가 위의 표와 같고, 의뢰받은 금액이 4578원이라면, 최소의 비용으로 4578원어치의 동전을 생산하는 방법은 다음과 같습니다.

화폐 단위(원)   생산 단가(원)   생산 수량(개)   생산 비용(원)   생산 화폐 가치(원)
1   1   3   1 x 3 = 3   1 x 3 = 3
5   4   5   4 x 5 = 20   5 x 5 = 25
10   99   0   99 x 0 = 0   10 x 0 = 0
50   35   1   35 x 1 = 35   50 x 1 = 50
100   50   45   50 x 45 = 2250   100 x 45 = 4500
500   1000   0   1000 x 0 = 0   500 x 0 = 0
총 비용         3 + 20 + 35 + 2250 = 2308   
총 화폐 가치            3 + 25 + 50 + 4500 = 4578
즉, 1원짜리 동전을 3개, 5원짜리 동전을 5개, 50원짜리 동전을 1개, 100원짜리 동전을 45개 생산하면 2308원이라는 최소 비용으로 4578원어치의 동전을 생산할 수 있습니다. 2308원보다 적은 비용으로 4578원어치의 동전을 생산할 수 있는 방법은 없습니다.

공장이 생산해야 하는 금액을 나타내는 정수 money, 6종류 동전의 생산 단가를 나타내는 1차원 정수 배열 costs가 매개변수로 주어집니다. money원만큼의 동전을 최소 비용으로 생산했을 때, 그 최소 비용을 return 하도록 solution 함수를 완성해주세요.

제한사항
1 ≤ money ≤ 1,000,000
costs의 길이 = 6
1 ≤ costs의 원소 ≤ 5,000
costs[0] ~ costs[5]은 차례대로 1원, 5원, 10원, 50원, 100원, 500원짜리 동전의 생산 단가를 담고 있습니다.
입출력 예
money   costs   result
4578   [1, 4, 99, 35, 50, 1000]   2308
1999   [2, 11, 20, 100, 200, 600]   2798
입출력 예 설명
입출력 예 #1

문제 예시와 같습니다.

입출력 예 #2

화폐 단위(원)   생산 단가(원)   생산 수량(개)   생산 비용(원)   생산 화폐 가치(원)
1   2   9   2 x 9 = 18   1 x 9 = 9
5   11   0   11 x 0 = 0   5 x 0 = 0
10   20   4   20 x 4 = 80   10 x 4 = 40
50   100   1   100 x 1 = 100   50 x 1 = 50
100   1200   4   200 x 4 = 800   100 x 4 = 400
500   600   3   600 x 3 = 1800   500 x 3 = 1500
총 비용         18 + 80 + 100 + 800 +1800 = 2798   
총 화폐 가치            9 + 40 + 50 + 400 + 1500 = 1999
2798원의 최소 비용으로 1999원어치의 동전을 생산할 수 있습니다.
500원짜리 동전을 4개 생산하면 2400원(600 x 4 = 2400)의 비용으로 2000원어치의 동전을 생산할 수 있습니다. 하지만, 공장이 생산해야 하는 금액은 정확히 1999원이어야 합니다. 즉, 주어진 금액을 초과하는 금액을 더 싼 비용으로 생산할 수 있다고 하여도, 그것은 정답으로 인정되지 않습니다.
 """
""" money = 4578
costs = [1, 4, 99, 35, 50, 1000]

def solution(money, costs):
    m_list = [1,5,10,50,100,500]
    m_dict = dict()
    for i, j in zip(m_list,costs):
        m_dict[i]=j
    order = sorted(m_dict,key=lambda x: m_dict[x]/x)
    answer = 0 
    for i in order: 
        num, money = money//i, money%i
        answer += num*m_dict[i]
    return answer """
""" 문제 설명
자연수 n과 시계/반시계 방향을 결정하는 boolean 값 clockwise가 주어집니다. 입출력 예 설명의 그림과 같이 소용돌이 모양(clockwise가 참이면 시계방향, 거짓이면 반시계방향)으로 n x n 정수 배열을 채워 return 하도록 solution 함수를 완성해주세요.

제한사항
n은 1 이상 1,000 이하입니다.
입출력 예(파이썬을 제외한 언어)
n   clockwise   result
5   true   
[[1,2,3,4,1]
,[4,5,6,5,2]
,[3,6,7,6,3]
,[2,5,6,5,4]
,[1,4,3,2,1]]


6   false   
[[1,5,4,3,2,1]
,[2,6,8,7,6,5]
,[3,7,9,9,8,4]
,[4,8,9,9,7,3]
,[5,6,7,8,6,2]
,[1,2,3,4,5,1]]

9   false   처음에는  n - 2칸을 가고, 그다음은 1칸만 줄어들고, 그 다음은 2칸씩 줄어든다.
처음 주어진 n 이 짝수면 그대로 정답, 홀수면 가운데가 최신화가 안된다.
[[1,8, 7, 6, 5, 4, 3,2,1]
,[2,9,14,13,12,11,10,9,8]
,[3,10,15,18,17,16,15,14,7]
,[4,11,16,19,20,19,18,13,6]
,[5,12,17,20,21,20,17,12,5]
,[6,13,18,19,20,19,16,11,4]
,[7,14,15,16,17,18,15,10,3]
,[8,9,10,11,12,13,14,9,2]
,[1,2,3,4,5,6,7,8,1]]

입출력 예(파이썬)
n   clockwise   result
5   True   [[1,2,3,4,1],[4,5,6,5,2],[3,6,7,6,3],[2,5,6,5,4],[1,4,3,2,1]]
6   False   [[1,5,4,3,2,1],[2,6,8,7,6,5],[3,7,9,9,8,4],[4,8,9,9,7,3],[5,6,7,8,6,2],[1,2,3,4,5,1]]
9   False   [[1,8,7,6,5,4,3,2,1],[2,9,14,13,12,11,10,9,8],[3,10,15,18,17,16,15,14,7],[4,11,16,19,20,19,18,13,6],[5,12,17,20,21,20,17,12,5],[6,13,18,19,20,19,16,11,4],[7,14,15,16,17,18,15,10,3],[8,9,10,11,12,13,14,9,2],[1,2,3,4,5,6,7,8,1]]
입출력 예 설명
입출력 예 #1

clockwise가 참이므로, 소용돌이를 시계방향으로 돌려야 합니다.
다음 그림은 5x5 정사각형을 시계방향 소용돌이 모양으로 채운 모습입니다.
ex1.png
입출력 예 #2

clockwise가 거짓이므로, 소용돌이를 반시계방향으로 돌려야 합니다.
다음 그림은 6x6 정사각형을 반시계방향 소용돌이 모양으로 채운 모습입니다.
ex2.png
입출력 예 #3

clockwise가 거짓이므로, 소용돌이를 반시계방향으로 돌려야 합니다.
다음 그림은 9x9 정사각형을 반시계방향 소용돌이 모양으로 채운 모습입니다. """
""" 
n = 13
clockwise = False


def solution(n, clockwise):
    v = (0,0,n-2,0,True)
    v1, v2, v3 = (n-1,0,n-2,1,True),(n-1,n-1,n-2,2,True),(0,n-1,n-2,3,True)


    def go(x,y,num,di,first):
        if first: next_num = num - 1
        else: next_num = num -2
        while num:
            now = answer[y][x]
            direction = [(x+1,y),(x,y+1),(x-1,y),(x,y-1)]
            x,y = direction[di]
            answer[y][x] = now + 1
            num -= 1
        return x,y,next_num,(di+1)%4,False

    answer = [[1]*n for i in range(n)]
    go_num = n
    while go_num>0:
        v = go(*v)
        v1 = go(*v1)
        v2 = go(*v2)
        v3 = go(*v3)
        go_num = v[2]

    if n%2==1:
        center = n//2
        answer[center][center]=n*n//4+1

    if clockwise: return answer
    else: return answer[::-1]

import numpy as np

print(np.array(solution(n,True))) """



""" 문제 설명
가로 1칸, 세로 1칸의 크기를 갖는 정사각형으로 이루어진 가로 width칸, 세로 height칸의 격자가 있습니다. 일부 정사각형에는 "왼쪽 위의 점과 오른쪽 아래점을 잇는" 대각선이 있습니다. 이 격자에서 다음 조건을 만족하는 경로의 개수를 구하고자 합니다.

좌측 하단의 끝점에서 우측 상단의 끝점으로 가는 경로입니다.
대각선을 정확히 1번 이용해야 합니다.
1, 2번 조건을 만족하는 전제 하에서 최단거리 경로여야 합니다.


예를 들어, 다음 그림은 한 격자가 주어졌을 때, 해당 격자에서 1~3번 조건을 만족하는 경로를 모두 나타낸 것입니다.

ex1.png

격자의 가로 길이 width, 세로 길이 height, 대각선이 위치한 정사각형의 정보 diagonals가 매개변수로 주어집니다. 주어진 조건을 모두 만족하는 경로의 개수를 10,000,019로 나눈 나머지를 return 하도록 solution 함수를 완성해주세요.

제한사항
1 ≤ width ≤ 250
1 ≤ height ≤ 250
1 ≤ diagonals의 길이 ≤ width × height
diagonals의 각 행은 두 정수 [x, y]로 이루어져 있으며, 왼쪽에서부터 x번째, 아래에서부터 y번째 사각형에 대각선이 있음을 의미합니다.
1 ≤ x ≤ width
1 ≤ y ≤ height
똑같은 (x, y) 순서쌍은 2번 이상 등장하지 않습니다.
입출력 예
width   height   diagonals   result
2   2   [[1,1],[2,2]]   12
51   37   [[17,19]]   3225685
입출력 예 설명
입출력 예 #1

문제 예시와 같습니다.
입출력 예 #2

실제 경우의 수는 776,469,491,667,984,972,858,000 가지이므로, 이를 10,000,019로 나눈 나머지인 3,225,685를 return 해야 합니다. """
# 776,469,491,667,984,972,858,000
# - > 7.76469491667984e23
""" from functools import reduce
DIVNUM = 10000019
def fact(num):
    answer = 1
    for i in range(1,num+1):
        answer *= i
    return answer # reduce(lambda x, y: x*y, list(range(1,num+1)), 1) # 안빠름

def solution(width, height, diagonals):
    answer = 0
    
    for i, j in diagonals:
        x, y = width - i, height - j
        answer += (fact(x+y+1)//fact(x)//fact(y+1)%DIVNUM*fact(i+j-1)//fact(i-1)//fact(j)%DIVNUM \
            + fact(x+y+1)//fact(x+1)//fact(y)%DIVNUM*fact(i+j-1)//fact(i)//fact(j-1)%DIVNUM)%DIVNUM
    return answer % DIVNUM
 """
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
nlist = [5,4]
edgeslist = [[[0,1],[0,2],[1,3],[1,4]],\
             [[2,3],[0,1],[1,2]]]
# 0-1-3-4
#  -2
from itertools import permutations

def distance(a: set, b: set) -> int:
    a_ = a - b
    b_ = b - a
    return len(a_)+len(b_)



def aligncheck(nodes, tree) -> bool:
    a,b,c = nodes
    aroot = set()
    broot = set()
    croot = set()
    # a  3 1 0 
    # b  1 0 
    # c  2 0
    while type(a)==int:
        aroot.add(a)
        a = tree[a]
    while type(b)==int:
        broot.add(b)
        b = tree[b]
    while type(c)==int:
        croot.add(c)
        c = tree[c]
    # print(nodes)
    # print(distance(aroot,broot),distance(broot,croot),distance(broot,croot))
    if distance(aroot,broot) + distance(broot,croot) == distance(aroot,croot): return True
    else: return False


def solutions(n, edges):
    answer = 0
    tree = [None for _ in range(n)]

    for i, j in edges:
        tree[j] = i
    
    for i in permutations(range(n), 3):
        answer += aligncheck(i, tree)

    return answer


count = 1 
for i, j in zip(nlist, edgeslist):
    print(f"                                                           {count}번 정답:",end='')
    print(solutions(i,j))
    count += 1
