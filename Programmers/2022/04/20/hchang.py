from itertools import permutations
import re
with open('data/hchang','r') as f:
    exp, answer = f.read().split()
# def go(exp, op):

#     return re.search(f'[\d]+\\{op}[\d]+|\(\-[\d]+\)\\{op}[\d]+|\
#                         [\d]+\\{op}\(\-[\d]+\)|\(\-[\d]+\)\\{op}\(\-[\d]+\)', exp)
# a = '12+(-3)+12+12'

# while pos:=go(a,'+'):
#     print(a)
#     check_num = eval(a[pos.start():pos.end()])
#     if check_num < 0:
#         a = a[:pos.start()]+'('+str(check_num)+')'+a[pos.end():]
#     else: a = a[:pos.start()]+str(check_num)+a[pos.end():]
def solution(expression):
    def go(exp, op):
        ps0 = re.search(f'[\d]+\\{op}[\d]+', exp)
        ps1 = re.search(f'\(\-[\d]+\)\\{op}[\d]+', exp)
        ps2 = re.search(f'[\d]+\\{op}\(\-[\d]+\)', exp)
        ps3 = re.search(f'\(\-[\d]+\)\\{op}\(\-[\d]+\)', exp)
        lst = [ps0,ps1,ps2,ps3]
        lstval = [i.start() if i else 100 for i in lst]
        return lst[lstval.index(min(lstval))]
        
    result = []
    for i in permutations('+-*',3):
        # print(i)
        run = expression
        for j in i:
            while pos := go(run,j):
                if i==('*','+','-'): print(run)
                check_num = eval(run[pos.start():pos.end()])
                if check_num < 0:
                    run = run[:pos.start()]+'('+str(check_num)+')'+run[pos.end():]
                else: run = run[:pos.start()]+str(check_num)+run[pos.end():]
        result.append(abs(int(eval(run))))
    print(result)
    answer = max(result)
    return answer

anw = solution(exp)

if anw==int(answer):
    print('정답!')
else: print('땡!!')