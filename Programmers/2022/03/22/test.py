from audioop import reverse


x1 = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"],	[2,3,4],	["AC", "ACDE", "BCFG", "CDE"]
x2 = ["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"],	[2,3,5],	["ACD", "AD", "ADE", "CD", "XYZ"]
x3 = ["XYZ", "XWY", "WXA"],	[2,3,4],	["WX", "XY"]
X = [x1,x2,x3]

def dfs_num(lst, num, eliments=[]):
    if len(eliments) == num:
        yield eliments[:]
    for i, j in enumerate(lst):
        eliments.append(j)
        yield from dfs_num(lst[i+1:], num, eliments)
        eliments.pop()

def most_common(orders, num):
    max_menu = {}
    for foods in orders:
        for i in dfs_num(sorted(foods), num):
            try: max_menu[''.join(i)] += 1
            except: max_menu[''.join(i)] = 1
    sort_menu = sorted(max_menu, key=lambda x: max_menu[x], reverse=True)
    return [i for i in sort_menu if max_menu[i]==max_menu[sort_menu[0]] and max_menu[i] >= 2]


def solution(orders, course):
    answer = []
    for i in course:
        answer += most_common(orders, i)
    return sorted(answer)

# for i in dfs_num([1,3,4,5],3):
#     print(i)
for i in X:
    orders, course, answer = i
    result = solution(orders, course)
    print(result, answer)
    if result == answer: print("정답")
    else: print('땡')