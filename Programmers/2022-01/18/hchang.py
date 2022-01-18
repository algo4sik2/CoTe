from collections import deque



def solution(progresses, speeds):
    answer = []
    while progresses:
        count = 0 
        task = []
        new_speeds = []
        able = True
        for i, j in zip(progresses, speeds):
            if i >= 100 and able:
                count += 1
                continue
            else: 
                task.append(i+j)
                new_speeds.append(j)
                able = False
        progresses = task
        speeds = new_speeds
        if count != 0:
            answer.append(count)
    
    # tasks = deque(progresses)
    # speeds = deque(speeds)
    # answer = []
    # while tasks:
    #     count = 0
    #     while tasks:
    #         if tasks[0]>=100:
    #             tasks.popleft()
    #             speeds.popleft()
    #             count +=1
    #         else: break
    #     if count !=0: answer.append(count)
    #     tasks = deque(map(lambda x: x + speeds[tasks.index(x)],tasks))
        

    return answer
