scovile, K, result = [1, 2, 3, 9, 10, 12], 7, 2

import heapq


def solution(scovile, k):
    heapq.heapify(scovile)
    count = 0
    while True:
        if len(scovile)==1 and scovile[0] < k:
            return -1
        el1 = heapq.heappop(scovile)
        if el1 >= k: break
        el2 = heapq.heappop(scovile)
        new = el1 + el2*2
        count += 1
        heapq.heappush(scovile, new)

    answer = count
    return answer

print(solution(scovile, K))