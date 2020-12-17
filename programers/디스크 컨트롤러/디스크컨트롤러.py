from collections import deque


# 첫번째 시도 - 대실패

def solution(jobs):
    num_of_work = len(jobs)
    sorted_jobs = sorted(jobs, reverse=True)
    first = sorted_jobs.pop() # 처음 작업
    curr_time = first[0] + first[1] # 현재시간

    waiting_works = sorted(sorted_jobs, key=lambda x: x[1])

    waiting_works = deque(waiting_works)
    consumed_time = [curr_time]

    while waiting_works:
        work = waiting_works.popleft()

        if curr_time < work[0]:
            waiting_works.append(work)
            continue

        prev_time = curr_time
        curr_time += work[1]
        consumed_time.append(work[1] + prev_time - work[0])
    return sum(consumed_time)//num_of_work


# 두번째 시도
def solution2(jobs):

    return 1


print(solution([[0, 3], [1, 9], [2, 6]])) # result 9
print(solution([[0, 10]])) # result 10
print(solution([[1, 4], [0, 2], [3, 2], [4, 1]])) # result 4
print(solution([[1, 1], [3, 2], [4, 1], [5, 3]])) # result 2