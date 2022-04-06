""" C번 - 나는 정말 휘파람을 못 불어
시간 제한	메모리 제한
1 초	512 MB
문제
휘파람을 불지 못하는 시루는 휘파람을 불기 위해 수없이 많이 시도했지만 항상 실패한다. 시루의 휘파람 연습을 도와주고 있는 루시는, 시루가 휘파람과 비슷한 소리를 낼 때마다 사탕을 주기로 했다.

시루의 입에서 나온 소리는 대문자로 구성된 문자열 $S$로 나타낼 수 있다. 루시는 문자열 $S$에서 휘파람과 비슷한 소리, 즉 '유사 휘파람 문자열'의 개수를 구해야 한다. '유사 휘파람 문자열'은 다음과 같이 정의한다.

WHEE 는 '유사 휘파람 문자열'이다.
'유사 휘파람 문자열' 뒤에 E 를 붙인 것 또한 '유사 휘파람 문자열'이다.
'유사 휘파람 문자열'은 문자열 $S$ 상에서 연속하지 않아도 된다. 즉, $S$에서 '유사 휘파람 문자열'인 부분 수열(subsequence)의 개수를 구하면 된다.

시루는 수없이 많이 시도했기 때문에 $S$의 길이가 너무 길어졌다. 루시를 도와 시루에게 사탕을 몇 개 줘야 할지 계산해주자.

입력
첫째 줄에 문자열 $S$의 길이 $N$이 주어진다.

둘째 줄에 대문자로만 구성된 문자열 $S$가 주어진다.

출력
'유사 휘파람 문자열'인 부분 수열의 개수를 $1\,000\,000\,007(= 10^9+7)$로 나눈 나머지를 출력한다.

제한
 $1 \leq N \leq 200\,000$ 
 $S$는 대문자로만 구성되어 있다.
예제 입력 1 
8
WAHEWHEE
예제 출력 1 
6
W_HE__E_
W_HE___E
W_H___EE
W_HE__EE
W____HEE
____WHEE """
from math import factorial
from sys import stdin

stdin = open('data','r')


N = int(stdin.readline())
S = stdin.readline()

hdict = dict()

wnum = []
for i,j in enumerate(S):
    if j == 'W':
        wnum.append(i)
    if j=='H':
        for k in wnum:
            hdict[(k,i)] = 0
    if j=='E':
        for k in hdict.keys():
            hdict[k]+=1
total = 0
for i in hdict.values():
    if i < 2:
        continue
    total += 2**i - factorial(i)//factorial(1)//factorial(i-1) - 1
print(total)