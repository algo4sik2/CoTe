# 떡볶이 떡 만들기
# N: 떡 개수, M: 요청한 길이
# 떡의 개별 길이

import random
import sys
from time import time
# N = random.randint(1,1000000)
# data = [random.randint(1,1000000000) for _ in range(N)]
# M = random.randint(1,sum(data))

# with open('data/7-3.txt','w') as f:
#     f.write(str(N) + ' ' + str(M)+'\n')
#     f.write(' '.join(map(str, data)))

sys.stdin = open('data/7-3.txt', 'r')
st = time()

N, M = map(int, input().split())
Ejremf = list(map(int, input().split()))

def cutting(h):
    return sum([Ejr - h for Ejr in Ejremf if Ejr > h])

def find_h():
    answer = 0
    min_h = 0
    max_h = 1000000000
    while min_h < max_h:
        h = (min_h+max_h)//2
        m = cutting(h)
        if M <= m:
            answer = h
            min_h = h + 1
        else:
            max_h = h
    
    return answer



        # else:
        #     if M >= cutting(h - 1):
        #         return h
        #     else:
        #         max_h -= (m - M)//N

print(find_h())    
print(f"걸린시간: {time() - st}")
print(M, cutting(142676703))