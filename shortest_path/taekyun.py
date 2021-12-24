# 2.py

# 1->

# sol 1 -> k -> x:
# 1 -> k = 1 -> 2 -> k

def sol():

    INF = int(1e9)
    n, m = map(int, input().split())
    l = []

    board = [[INF for _ in range(n + 1)] for _ in range(n + 1)]

    for _ in range(m):
        x_, y_ = map(int, input().split())
        board[x_][y_] = 1
        board[y_][x_] = 1
    
    x, k = map(int, input().split())


    for k in range(1, n + 1):
        for x_ in range(1, n + 1):
            for y_ in range(1, n + 1):
                if board[x_][k] + board[k][y_] < board[x_][y_]:
                    board[x_][y_] = board[x_][k] + board[k][y_]
    
    print(board[1][k] + board[k][x] if board[1][k] + board[k][x] < INF else -1)

sol()