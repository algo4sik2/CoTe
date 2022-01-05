


numlist= ['zero','one','two','three','four','five','six','seven','eight','nine']
numdict = {}

for i,j in enumerate(numlist):
    numdict[j] = i
      
# print('1'.isdigit())

def solution(s):
    
    num = ""
    intnumlist = []
    for i in s:
        if i.isdigit():
            intnumlist.append(i)
        else:
            num += i
            if num in numlist:
                intnum = numdict[num]
                intnumlist.append(str(intnum))
                num = ''
        
    answer = ''.join(intnumlist)
    return int(answer)