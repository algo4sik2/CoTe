def solution(board, moves):
    box = [0]
    answer = 0
    for move in moves:
        for i in range(len(board)):
            if board[i][move-1] != 0:
                box.append(board[i][move-1])
                board[i][move-1] = 0
                if box[-1] == box[-2]:
                    answer += 2
                    box.pop()
                    box.pop()
                break
    return answer