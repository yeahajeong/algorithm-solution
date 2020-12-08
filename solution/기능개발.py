# 스택 / 큐
import math


# 처음 제출 코드
def solution(progresses, speeds):
    answer = []
    works = [math.ceil((100 - progress) / speed) for progress, speed in zip(progresses, speeds)]
    working = []
    print(works)

    for work in works:
        if len(working) == 0:
            working = [work]
            com = work
        elif com >= work:
            working.append(work)
        else:
            answer.append(len(working))
            working = [work]
            com = work
    answer.append(len(working))
    return answer


# 다른 코드
def another_solution(progresses, speeds):
    answer = []
    task = 0
    prev_day = math.ceil((100 - progresses[0] / speeds[0]))

    for progress, speed in zip(progresses, speeds):
        now_day = math.ceil((100 - progress / speed))

        if prev_day >= now_day:
            task += 1
        else:
            answer.append(task)
            prev_day = now_day
            task = 1
    answer.append(task)
    return answer


progresses = [93, 30, 55]
speeds = [1, 30, 5]
print(another_solution(progresses, speeds))
