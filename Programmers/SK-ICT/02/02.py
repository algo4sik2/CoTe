from collections import deque

# whole_time과 요청시간 비교
# 요청시간이 더 뒤면 no_working으로 시간 기록
# writing = bool로 상태 확인
# write는 그냥 하고,
# read는 writing 상태에 따라 다르게 함.
# wait_cmd에 writing일때, read명령을 모아놓고, 후에 한꺼번에 실행하면서, runing_time을 받아놓음

arrs = [["1","2","4","3","3","4","1","5"],["1","1","1","1","1","1","1"]]
processeses = [["read 1 3 1 2","read 2 6 4 7","write 4 3 3 5 2","read 5 2 2 5","write 6 1 3 3 9", "read 9 1 0 7"],\
    ["write 1 12 1 5 8","read 2 3 0 2","read 5 5 1 2","read 7 5 2 5","write 13 4 0 1 3","write 19 3 3 5 5","read 30 4 0 6","read 32 3 1 5"]]


def solution(arr, processes) -> list:
    answer = []
    no_working_time = 0
    whole_time = 0
    wait_cmd = deque()
    writing = False
    
    def waited_cmd():
        runing_time = 0
        while wait_cmd:
            cmd = wait_cmd.popleft()
            if runing_time < int(cmd[2]): runing_time = int(cmd[2])
            answer.append(''.join(arr[int(cmd[3]):int(cmd[4])+1]))
        return runing_time

    for process in processes:
        process = process.split()
        if process[0]=='write':
            if whole_time < int(process[1]):
                runing_time = waited_cmd()
                whole_time += runing_time
            writing = True
            if whole_time < int(process[1]):
                no_working_time += int(process[1]) - whole_time
                whole_time = int(process[1]) + int(process[2])
            else:
                whole_time += int(process[2])
            arr[int(process[3]):int(process[4])+1] = [process[5]]*(int(process[4])+1-int(process[3]))
        
        elif not writing or whole_time < int(process[1]):
            if whole_time >= int(process[1]):
                whole_time = max(whole_time, int(process[1]) + int(process[2]))
                answer.append(''.join(arr[int(process[3]):int(process[4])+1]))
            else:
                writing = False
                runing_time = waited_cmd()
                whole_time += runing_time
                if whole_time < int(process[1]): no_working_time += int(process[1]) - whole_time
                whole_time = max(whole_time, int(process[1]) + int(process[2]))
                answer.append(''.join(arr[int(process[3]):int(process[4])+1]))

        else:
            wait_cmd.append(process)
    runing_time = waited_cmd()
    whole_time += runing_time
    whole_time -= no_working_time
    answer.append(str(whole_time))

    return answer

count = 0
for arr, processes in zip(arrs, processeses):
    count += 1
    print(f'{count}번 정답: ', end='')
    print(solution(arr,processes))


# def solution(arr, processes) -> list:
#     working = 0 
#     answer = []
#     wait_cmd = deque()
#     whole_time = 0
#     reading_time = 0
#     more_time = 0
#     first = True

#     # whole_time과 요청시간을 비교하여, 요청시간이 더 짧은건 read만 받아놓는다.
#     # write는 바로 넘긴다.
#     for process in processes:
#         process = process.split()
#         if first: 
#             first_time = process[1]
#             first = False
#         if int(process[1]) < whole_time and process[0]=='read':
#             wait_cmd.append(process)
#             continue
#         else:
#             if process[0]=='write' and whole_time >= int(process[1]): # write 처리
#                 whole_time += int(process[2])
#                 reading_time = 0
#                 arr[int(process[3]):int(process[4])+1] = [process[5]]*(int(process[4])+1-int(process[3]))
#                 continue
#             # read 밀린게 있으면 먼저 처리한다.
#             while wait_cmd:
#                 cmd = wait_cmd.popleft()
#                 time = int(cmd[2])
#                 if time > more_time: more_time = time
#                 answer.append(''.join(arr[int(cmd[3]):int(cmd[4])+1]))

#             if process[0]=='write': # write 처리
#                 if more_time: 
#                     whole_time += more_time
#                     more_time = 0
#                 if reading_time: whole_time = reading_time
#                 if whole_time < int(process[1]): whole_time = int(process[1]) + int(process[2])
#                 else: whole_time += int(process[2])
#                 reading_time = 0
#                 arr[int(process[3]):int(process[4])+1] = [process[5]]*(int(process[4])+1-int(process[3]))
#                 continue

#             # whole_time 이후 명령은 처리하되, read 반영하다가 write가 나오면 whole_time
#             # 최신화 한다.
#             if process[0]=='read':
#                 working += int(process[2])
#                 time = int(process[1]) + int(process[2])
#                 if time > reading_time: reading_time = time
#                 answer.append(''.join(arr[int(process[3]):int(process[4])+1]))

#     whole_time = max(reading_time,whole_time)
#     while wait_cmd:
#         cmd = wait_cmd.popleft()
#         time = int(cmd[2])
#         if time > more_time: more_time = time
#         answer.append(''.join(arr[int(cmd[3]):int(cmd[4])+1]))
#     whole_time += more_time
#     whole_time -= 
#     answer.append(str(whole_time))
#     return answer


#                 while waiting:
#                     cmd = waiting.popleft()
#                     if runtime > int(cmd[2]): runtime = int(cmd[2])
#                     answer.append(''.join(arr[int(cmd[3]):int(cmd[4])+1]))