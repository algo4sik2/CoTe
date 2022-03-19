import random
from time import time
from tqdm import tqdm

N = 999999
k = random.randint(100,999999)
numlist = [random.randrange(10) for _ in range(N)]
input_ = ''.join(map(str,numlist))


""" 
# 기존 풀이 -> stack과 que를 잘 활용하지 않았다. 시간 복잡도 고려 x
def solution(number, k):
    number = list(map(int,number))
    popnum = 0
    sortnum = sorted(number, reverse=True)
    for i in tqdm(range(len(number)-1)):
        i -= popnum
        for j in range(i+1):
            if number[i-j] < number[i+1-j] and k: 
                number.pop(i-j)
                k -= 1
                popnum += 1
            else: break
        if k==0 or sortnum==number: break
    if k:
        number = number[:-k]
    answer = ''.join(map(str,number))
    return answer
 """
from collections import deque

def solution(number, k):
    number_stack = []
    
    for i in number:
        check = True
        while number_stack and k and check:
            if number_stack[-1] < i:
                number_stack.pop()
                k -=1
            else: check = False
        number_stack.append(i)
    if k:
        number_stack = number_stack[:-k]
    answer = ''.join(map(str,number_stack))
    return answer


# with open('data/test','r') as f:
#     count = 0
#     for i in f.readlines():
#         count += 1
#         number, k, answer = i.split()
#         print(f'{count}번', solution(number, int(k))==answer,solution(number, int(k)), answer )
st = time()

output = solution(input_, k)

print(output)
print(time()-st)

# answer = input('저장하시겠습니까?(y/n) :')
# if answer == 'y':
#     with open('data/test1', 'a') as f:
#         f.write(input_ + ' ')
#         f.write(str(k)+' ')
#         f.write(output)

# with open('data/test', 'r') as f:
#     for i in f.readlines():
#         number, k, coanswer = i.split()
#         answer = solution(number, int(k))





















# def solution(number, k):
#     number = list(map(int,number))
#     for i in range(len(number)-1):
#         if k == 0: break
#         if number[i] < number[i+1]:
#             k -= 1
#             number[i], number[i+1] = number[i+1], number[i]
#     answer = ''.join(map(str,number))
#     return answer

# def solution(number, k):
#     number = list(map(int,number))
#     al = True
#     while k:
#         ex = True
#         if al:
#             for i in range(len(number)-1):
#                 if number[i] < number[i+1]: 
#                     number.pop(i)
#                     k -= 1
#                     ex = False
#                     break
#         if ex and k:
#             al = False
#             number.pop()
#             k -=1
#     answer = ''.join(map(str,number))
#     return answer