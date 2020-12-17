# 프로그래머스 lv4.버스여행
from _collections import deque


# 정류장을 찾는 함수
def search(src, sign):
    return deque([(src, dest) for dest, check in enumerate(sign) if check == 1])


def solution(n, signs):
    answer = [[0] * n for _ in range(n)]

    for start, sign in enumerate(signs):
        queue = search(start, sign)

        while queue:
            src, dest = queue.popleft()
            if answer[src][dest] == 0:
                queue += search(start, signs[dest])
                answer[src][dest] = 1
    return answer

