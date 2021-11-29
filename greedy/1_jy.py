# < 거스름돈 문제 >
# 손님에게 거슬러 줘야 할 돈이 N원일 때 거슬러 줘야 할 동전의 최소 갯수를 구하라.


n = 1260
cnt = 0
coins = [500, 100, 50, 10]

for coin in coins:
    cnt += n // coin
    n %= coin
    
print(cnt)