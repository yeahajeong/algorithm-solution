from math import ceil
# 전체적으로 보자면 Queue의 형태를 사용해여 해결 가능
# 조건이 맞으면 맨 앞의 값부터 빠져나오기 때문에 FIFO의 형태를 가진다


# 1. O(n^2)의 풀이
def solution1(progresses, speeds):
    answer = []
    while progresses:
        for index in range(len(progresses)):
            progresses[index] += speeds[index]

        if progresses[0] >= 100:
            count = 0
            while progresses and progresses[0] >= 100:
                progresses.pop(0)  # dequeue를 쓸때와 차이 설명
                speeds.pop(0)
                count += 1
            answer.append(count)
    return answer


# 2. O(n) 풀이
def solution2(progresses, speeds):
    answer = [] # 리턴할 리스트 변수
    # 핵심 아이디어는 나눗셈과 올림을 이용하는 것!
    max_duration = ceil((100 - progresses[0]) / speeds[0])
    count = 0

    for progress, speed in zip(progresses, speeds):
        duration = ceil((100 - progress) / speed)
        # duration = -(-(100 - progress) // speed) # 이러한 방식도 있다.

        if max_duration < duration:
            answer.append(count)
            count = 0
            max_duration = duration
        count += 1

    if count > 0:
        answer.append(count)

    return answer


# 특이한 풀이
def solution3(progresses, speeds):
    answer = [[ceil((100-progresses[0]) / speeds[0]), 0]]

    for index, (progress, speed) in enumerate(zip(progresses, speeds)):
        duration = ceil((100 - progress) / speed)
        if answer[-1][0] < duration:
            answer.append([duration, 0])
        answer[-1][1] += 1

    return [i[1] for i in answer]

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
