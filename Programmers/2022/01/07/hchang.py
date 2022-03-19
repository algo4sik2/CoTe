
print("is".__dir__())

def solution(dartResult):
    compute = []
    two_num = False

    for i in dartResult:
        if i.isdigit():
            if not two_num:
                compute.append(int(i))
                two_num = True
            else:
                compute[-1] = int(str(compute[-1]) + i)
                two_num = False
        else:
            two_num = False
            if i == 'S':continue
            if i == 'D':
                compute[-1] = compute[-1]**2
                continue
            if i == 'T':
                compute[-1] = compute[-1]**3
                continue
            if i == '*':
                if len(compute) > 1:
                    compute[-2:] = compute[-2]*2, compute[-1]*2
                else:
                    compute[-1] = compute[-1]*2
                continue

            if i == '#':
                compute[-1] = compute[-1]*(-1)

    answer = sum(compute)
    return answer
