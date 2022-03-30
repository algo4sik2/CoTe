from collections import deque

def shift(deq, idx):
    for _ in range(idx):
        deq.append(deq.popleft())
    return deq


def solution(priorities, location):
    index_dir = [(val, idx) for idx, val in enumerate(priorities)]
    deq = deque(index_dir)
    while (current_max := max(deq, key=lambda x: x[0]))[1] != location:
        if deq[0] != current_max:
            deq = shift(deq, deq.index(current_max))
        deq.popleft()
    return len(priorities) - len(deq) + 1
