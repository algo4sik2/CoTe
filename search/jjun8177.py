# 5-2

n = int(input())
me = list(map(int, input().split()))

m = int(input())
you = list(map(int, input().split()))

me.sort()

answer = []

def bs(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
    
        if array[mid] == target:
            return mid
    
        elif array[mid] > target:
            end = mid - 1
        
        else:
            start = mid + 1
        
        return None   

    
for i in you:
    result = bs(me, i, 0, m-1)
    
    if result == None:
        answer.append('no')
    else:
        answer.append('yes')
        
for i in answer:
    print(i, end = ' ')
    
    


#5-3
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
    
    
        

