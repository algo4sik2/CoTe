# 두 배열의 원소 교체

n, k = map(int, input().split())


a = list((map(int, input().split())))
b = list((map(int, input().split())))
    
sum = 0
 
a = sorted(a)
b = sorted(b, reverse=True)

for i in range(k):
    a[i], b[i] = b[i], a[i]
    
for i in a:
    sum += i
    
print(sum)