import time
start_time = time.time()

n, m = map(int, input().split())
min_list = []
for _ in range(n):
  cand = map(int, input().split())
  min_list.append(min(cand))
print(max(min_list))

end_time = time.time()
print(f'time : {start_time - end_time}')