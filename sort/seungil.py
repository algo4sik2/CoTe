import sys
sys.stdin = open("input.txt", "r", encoding='utf-8')

# 실전문제 2 위에서 아래로(p.178)
n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))

arr.sort(reverse=True)
for i in arr:
    print(i, end=' ')

#----------------------------------------------#

# 실전문제 3 성적이 낮은 순서로 학생 출력하기(p.180)
n = int(input())
students = []
for _ in range(n):
    name, score = input().split()
    students.append((name, int(score)))

students.sort(key=lambda x: x[1])
for i in students:
    print(i[0], end=' ')

#----------------------------------------------#

# 실전문제 4 두 배열의 원소 교체(p.182)
n, k = map(int, input().split())
a, b = list(map(int, input().split())), list(map(int, input().split()))

for _ in range(k):
    a.sort()
    b.sort()
    a[0], b[-1] = b[-1], a[0]

print(sum(a))

