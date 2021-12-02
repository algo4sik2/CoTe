# from itertools import permutations

col, row = input()
col, row = ord(col) - ord('a') + 1, int(row)

direct = [(-2, -1), (-2, 1), (2, -1), (2, 1), (1, 2), (-1, 2), (1, -2), (-1, -2)]
cnt = 8

def inval(val):
    return val < 1 or val > 8

for x, y in direct:
    if inval(col + x) or inval(col + y):
        cnt -= 1
print(cnt)

# direct = [(x,y) for x,y in direct if inval(col + x) or inval(col + y)]
# print(len(direct))
