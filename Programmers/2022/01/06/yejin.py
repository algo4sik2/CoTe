def solution(n, arr1, arr2):
    answer = []
    
    for i in range(0, n):        
        # 비트 연산(or) 후 이진법으로 변환
        s = bin(arr1[i]|arr2[i])[2:]
        
        # '#'과 ' '으로 변환
        new_s = s.replace('1','#')
        new_s2 = new_s.replace('0',' ')
        
        # n자리 수 만큼 공백 채우기
        padding = ' '
        answer.append(f'{new_s2:{padding}>{n}}')
    
    return answer