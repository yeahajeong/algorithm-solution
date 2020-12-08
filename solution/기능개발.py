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
            comm = work
        elif comm >= work:
            working.append(work)
        else:
            answer.append(len(working))
            working = [work]
            comm = work
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


# 다른 사람이 푼 코드
def another_solution2(progresses, speeds):
    Q = []
    for p, s in zip(progresses, speeds):
        print(Q)
        if len(Q) == 0 or Q[-1][0] < -((p-100)//s):
            Q.append([-((p-100)//s), 1])
        else:
            Q[-1][1] += 1
        print(Q)
        print("")
    return [q[1] for q in Q]


progresses = [93, 30, 55]
speeds = [1, 30, 5]
print(another_solution2(progresses, speeds))
