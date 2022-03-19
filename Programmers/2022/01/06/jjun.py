def solution(n, arr1, arr2):
    
    temp = []
    answer = []
    for i,j in zip(arr1, arr2):
        temp.append(format((i|j), 'b'))

    for i in temp:
        i = i.replace('1','#')
        i = i.replace('0',' ')
        
        while (len(i) < n):
            i = ' ' + i
        
        answer.append(i)


    return answer

