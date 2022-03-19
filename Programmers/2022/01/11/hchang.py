def solution(board, moves):
    container = [-1]
    count = 0
    for i in moves:
        for j in board:
            if j[i-1]!=0:
                pic = j[i-1]
                j[i-1] = 0
                print(pic)
                container.append(pic)
                if container[-2]==container[-1]:
                    count += 1
                    container= container[:-2]
                break
    answer = count * 2
    return answer
