# 숫자 문자열과 영단어

def solution(s):
    
    answer = ''
    temp = ''
    num_dict = {'0':'zero', '1':'one', '2':'two', '3':'three', '4':'four',
               '5':'five', '6':'six', '7':'seven', '8':'eight', '9':'nine'}
    
    for word in s:
        if word in '0123456789':
            answer += word
        
        else:
            temp += word
            for (key, value) in num_dict.items():
                if value in temp:
                    answer += key
                    temp = ''
    return int(answer)