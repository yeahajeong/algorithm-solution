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