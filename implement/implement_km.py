
# 럭키스트레이트

n = input ()
summary = 0

length = len(n) 
summary = 0


for i i n range (length // 2):
    summary += int (n[i])


for i in range(length // 2, length):
    summary -= int (n[i])


if summary = = 0 :

    print ("LUCKY") 

else:
    print ("READY")