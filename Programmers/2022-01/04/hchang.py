# N [1,500]
# len(stages) [1, 200000] 사용자 수
# stages [1, N + 1]


def solution(N, stages):
    loss = {}
    for i in range(1,N+1):
        if len([j for j in stages if j >= i]) == 0:
            loss[i] = 0
        else:
            loss[i] = len([j for j in stages if j == i])/len([j for j in stages if j >= i])
    answer = sorted(loss,key=lambda x: loss[x], reverse=True)
    return answer