def solution(numbers, hand):
    
    point = {1:[0,0], 2:[0,1], 3:[0,2],
            4:[1,0], 5:[1,1], 6:[1,2],
            7:[2,0], 8:[2,1], 9:[2,2],
            '*':[3,0], 0:[3,1], '#':[3,2]}
    answer = ''
    left, right = '*', '#'
    
    for num in numbers:
        if str(num) in '147':
            left = num
            answer += 'L'
        elif str(num) in '369':
            right = num
            answer += 'R'
        else:
            if (abs(point[num][0] - point[left][0]) + abs(point[num][1] - point[left][1])) > (abs(point[num][0] - point[right][0]) + abs(point[num][1] - point[right][1])):
                right = num
                answer += 'R'
            elif (abs(point[num][0] - point[left][0]) + abs(point[num][1] - point[left][1])) < (abs(point[num][0] - point[right][0]) + abs(point[num][1] - point[right][1])):
                left = num
                answer += 'L'
            else:
                if hand == 'left':
                    left = num
                    answer += 'L'
                else:
                    right = num
                    answer += 'R'
    return answer