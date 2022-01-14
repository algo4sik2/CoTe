def dist(l_hand, r_hand, n, hand):
    l_dist = abs(l_hand - n) // 3 + abs(l_hand - n) % 3
    r_dist = abs(r_hand - n) // 3 + abs(r_hand - n) % 3
    return 'L' if (l_dist < r_dist) or ((l_dist == r_dist) and hand == 'left') else 'R'
    

def solution(numbers, hand):
    l_hand, r_hand  = 10, 12
    answer = ''
    for n in numbers:
        if n == 0:
            n = 11
        if n in [1, 4, 7]:
            answer += 'L'
            l_hand = n
        elif n in [3, 6, 9]:
            answer += 'R'
            r_hand = n
        else:
            answer += dist(l_hand - 1, r_hand - 1, n - 1, hand)
            if answer[-1] == 'L':
                l_hand = n
            else:
                r_hand = n
    return answer