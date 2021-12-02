n = int(input())
a_list = iter(input().split())
x,y = 1,1
for a in a_list:
    if a == 'L' and x > 1: x -= 1
    elif a == 'R' and x < n: x += 1
    elif a == 'U' and y > 1: y -= 1
    elif a == 'D' and y < n: y += 1

# for point in a_list:
#     match point:
#         case 'L' if x > 1: x -= 1
#         case 'R' if x < n: x += 1
#         case 'U' if y > 1: y -= 1
#         case 'D' if y < n: y += 1

print(y,x)