
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
    
    --------------------------------------
    -----------------------------------------
    
    
    def solution (s):
    answer = len(s)

    for step in range(1, len(s) // 2 + 1)

        compressed = "" 

        prev = s[0:step] 
        count = 1

    for j in range(step, len(s), step):

        count += 1

    else

        compressed += str(count ) + prev 
        prev = s[j :j + step] 
        count = 1

    compressed += str(count) + prev if count >= 2 else prev

    answer = min (answer, len(compressed))

return answer
