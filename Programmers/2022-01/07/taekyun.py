def solution(dartResult):
    point, bonus, option = [], [], []
    a = {'S':1, 'D':2, 'T':3}
    b = {'*':2, '#':-1}
    i = 0
    lst = []
    while i < len(dartResult):
        if dartResult[i] == '1' and dartResult[i + 1] == '0':
            point.append(int(dartResult[i] + dartResult[i + 1]))
            i += 1
        else:
            point.append(int(dartResult[i]))
        i += 1
        bonus.append(a[dartResult[i]])
        i += 1
        if not i < len(dartResult):
            option.append(1)
        elif dartResult[i] in b:
            option.append(b[dartResult[i]])
            i += 1 
        else:
            option.append(1)
    for i in range(3):
        if option[i] == 2 and i != 0:
            lst[-1] = lst[-1] * 2
        lst.append(point[i] ** bonus[i] * option[i])
    print(lst)
    return sum(lst)