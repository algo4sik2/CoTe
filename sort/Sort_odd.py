
# 선택 정렬
# array = [7,5,9,0,3,1,6,2,4,8]
# for i in range(len(array)):
#     min_index = i
#     for j in range(i+1,len(array)):
#         if array[min_index] > array[j]:
#             min_index = j
#
#     array[i],array[min_index] = array[min_index], array[i]

# print(array)

# array = [3,5]
# array[0],array[1] = array[1],array[0]
#
# print(array)

# 삽입 정렬
# for i in range(1,len(array)):
#     for j in range(i,0,-1):
#         if array[j] < array[j-1]:
#             array[j],array[j-1] = array[j-1],array[j]
#         else:
#             break
#
# print(array)

# # 퀵 정렬
# def quick_sort(array,start,end):
#     if start >= end:
#         return
#     pivot = start

#------------------------실전 문제 1. 위에서 아래로--------------------------
# a = list(map(int,input().split()))
# a.sort()
# a.reverse()
# for i in range(len(a)):
#     print(a[i],end=" ")
#
# #----------------------------------답안-----------------------------------
# array = []
# n = int(input())
#
# for i in range(n):
#     array.append(int(input()))
#
# array.sort(), array.reverse()
#
# for i in range(array):
#     print(i, end=" ")

#--------------------------실전문제 2. 성적이 낮은 순서로 학생 출력하기
# import sys
# # sys.stdin = open("input.txt", "r",encoding="UTF-8")
#
# n = int(input())
# array=[]
# for i in range(n):
#     a = input().split()
#     array.append((a[0],int(a[1])))
#
# array = sorted(array, key=lambda student: student[1])
#
# for b in array:
#     print(b[0], end=" ")

import sys
import time

sys.stdin = open("input.txt", "r",encoding="UTF-8")
start = time.time()

n,k = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
a.sort(),b.sort(reverse=True)

for i in range(k):
    if a[i] < b[i]:
        a[i],b[i] = b[i],a[i]
    else:
        break
print(sum(a))
end = time.time()
print(start-end)