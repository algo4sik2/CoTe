#!/usr/bin/env python
# coding: utf-8

# - 초보이기 때문에 하나하나 생각이 나는대로 끄적이면서 흐름을 따라가는 중입니다.

# In[6]:


#상하좌우 문제
#(1,1)에서 시작 
#정사각형 공간을 넘어가는 건 무시(if~continue)

N = int(input()) # 정사각형의 크기

x ,y =1,1 # 시작점

moves = input().split() # 이동하는 방향 대입

# L: y축 -1, R: y축 +1 , U: x축 -1 , D: x축 +1

dx = [0,0,-1,1] # x축에 영향을 주는 것

dy = [-1,1,0,0] # y축에 영향을 주는 것

types = ['L','R','U','D'] # 움직이는 방향 유형

for move in moves:
    
    for i in range(len(types)):# 방향 유형 삽입한 후에 인덱스 값 0,-1,1 추출
        
        if move == types[i]: # 인덱스 값 대입
            
            nx = x + dx[i] #변화한 x좌표
            
            ny = y + dy[i] # 변화한 y좌표
            
            
    if nx < 1 or ny <1 or nx > N or ny > N: # 무시하는 값
        
        continue
        
    x,y = nx , ny# 변화한 값 대입
        
print(x,y) # 변화한 값 출력
        


# In[7]:


# 시각 문제

# 숫자를 어떻게 셀 것인가 관점

# 시 , 분, 초 별로 따져서 갯수 세기 = for문 3개 쓰기

# 24, 60, 60 : range()함수 쓰기

# 신기한 포인트: 어떻게 3을 세야할까? 시,분,초를 합쳐서 하나의 숫자 형태로 만들어야한다.

N = int(input()) # 시 받는 수

count = 0 # 최종 경우의 수 센다

# 시,분,초가 나오게 되는 값 

for i in range(N+1):
    
    for j in range(60):
        
        for k in range(60):
            
            if str(i) =='3 ' or str(j) == '3' or str(k) == '3': #3이 있는 거 고르기
                count +=1
                
print(count)


# In[8]:


# 시각
# 둘의 차이가 뭘까요?
N = int(input()) # 시 받는 수

count = 0 # 최종 경우의 수 센다

# 시,분,초가 나오게 되는 값 

for i in range(N+1):
    
    for j in range(60):
        
        for k in range(60):
            
            if '3' in str(i) + str(j) + str(k): # 하나의 수로 만들어서 3이 있는 거 고르기 왜냐하면 시,분,초 어디에 있는지는 상관이 없음
                count +=1
                
print(count)


# In[8]:


#왕실의 나이트

# 상하좌우 문제와 유사한 flow 같습니다.

# 시작위치 잡기

# 행, 열을 잡아줘야한다 시작위치의 의거해서 왜냐하면 시작위치 기준으로 움직이는 경우의 수 변화

data = input() #입력 데이터는 int를 안해줄 경우 문자형으로 입력 받는다.

row = int(data([1])) # 1~8까지의 숫자
column = int(ord(data([0]))- int(ord('a')) +1               # 문자데이터 처리를 어떻게 할까..


# 나이트가 이동하는 경우의 수
# 상하좌우 L,R,U,D  느낌

# 근데 왜 이 값이 나오게 되는지 모르겠다.
# 왜 오류죠..ㅠ
             
moves = [
    
          (-2,-1),(-1,-2),(1,-2),(2,-1),
    
          (2,1), (1,2), (-1,2), (-2,1)
        ]

count = 0 # 경우의 수 합치기

# for문을 이용하여 이동방향 구하기
# next_row, next_column
# 상하좌우와 비슷하다

for move in moves:
    
    # 이동 변화
    next_row = row + move[0]
    next_column = column + move[1]
    
    # 상자 안에 있어야한다
    if next_row >=1 and next_row <= 8 and next_column >=1 and next_column <=8:
        count +=1
        
print(count)


# In[12]:


#럭키 스트레이트

# 입력값: 자릿수가 짝수개인 수만 입력이 되어야함, len함수 이용 그리고 2로 나누면 짝홀 구분 가능

# 입력값 기준으로 절반 나눈 뒤에 합쳐서 양쪽이 같으면 "LUCKY" 아니면 "READY"

N = input()# 입력조건

n = len(N) 

sum = 0 # 자릿수의 합

# 왼쪽의합
for i in range(n//2):
    
    sum += int(N[i])

# 오른쪽의합
for i in range(n//2, n):
    
    sum -= int(N[i])

# 둘의 나누기

if sum ==0:
    
    print("LUCKY")
    
else: 

    print("READY")


# In[ ]:


#문자열 재정렬

#입력값: 알파벳과 숫자

# 출력값: 알파벳을 순서대로 정렬한 후에 숫자들은 더해서 출력

# 알파벳과 숫자 분리(리스트)

# 알파벳과 숫자가 섞여 있어서 하나 하나 파악해서 숫자인 것과 알파벳인거 잡아야할 듯

# 숫자를 어떻게..해야..뒤로 보낼 수 있을까?


N = input() # 입력값

result = [] # 결과값 빈 리스트 만들기

figure = 0 # 숫자들 넣어서 합하기 위한 데이터



for i in N: # 숫자와 알파벳이 섞여있기 때문
    
    if i.isalpha():  # 알파벳
        
        result.append(i)

        
    else:  #숫자
        
        figure += int(i)
        
result.sort() #  정렬

