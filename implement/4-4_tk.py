# from functools import reduce

w, h = map(int, input().split())
x, y, direct = map(int, input().split())
game_map = []
for _ in range(h):
    game_map.append(list(map(int, input().split())))
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

def turn(n):
    if n == 0: return 3
    else: return n - 1

def seek(x, y, direct):
    for _ in range(4):
        # direct = direct - 1 if direct != 0 else 3
        direct = turn(direct)
        if game_map[y + dy[direct]][x + dx[direct]] == 0:
            return direct
    if game_map[y - dy[direct]][x - dx[direct]] == 1:
        return -1
    else:
        return seek(x - dx[direct], y - dy[direct], direct)
    

while True:
    game_map[y][x] = 2
    # print(game_map)
    if (direct := seek(x, y, direct)) != -1:
        x, y = x + dx[direct], y + dy[direct]
    else:
        break

# print(game_map)

cnt = 0
for m in game_map:
    cnt += m.count(2)
print(cnt)

# print(sum[m.count(2) for m in game_map])

# print(reduce(lambda x,y : x.count(2)+y.count(2), game_map))


# 현재 위치, 현재 보는 방향에서, direct를 idx -1만큼 한후 0인지 확인해봄
# 0이면 이동, 1이면 다시 돌아옴
# 네 방향 != 0 한칸뒤. (뒤가 1일시 break)