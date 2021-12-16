# 성적이 낮은 순서로 학생 출력하기

n = int(input())

names = []
scores = []

for i in range(n):
    name, score = input().split()
    names.append(name)
    scores.append(int(score))

for i in range(len(names)):
    for j in range(i):
        if scores[j] > scores[i]:
            names[j], names[i] = names[i], names[j]
            
print(names)