# 높이 h 지정. h보다 긴 떡은 h 윗부분 절단, 낮은 부분은 안 자름
# h = 15, in = [19, 14, 10, 17] -> [4, 0, 0, 2] -> 6

n, m = map(int, input().split())
tteok = list(map(int, input().split()))


cut = tteok[0]
cut_tteok = []


while (cut > 0):
    for i in tteok:
        if (i > cut):
            cut_tteok.append(i-cut)
        else:
            cut_tteok.append(0)
    
    sum = 0
    for i in cut_tteok:
        sum += i
       
    cut_tteok = []
     
    if sum == m:
        break
    
    else:
        cut -= 1
        
print(cut)
    
    
        

