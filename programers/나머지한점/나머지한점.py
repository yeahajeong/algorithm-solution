import collections


def solution(v):
    answer = []
    xs = []
    ys = []

    # x 좌표와 y좌표의 분리
    for x, y in v:
        xs.append(x)
        ys.append(y)

    # 숫자 세기 - Counter 활용
    xs = collections.Counter(xs)
    ys = collections.Counter(ys)

    # 홀수인 경우 answer에 담기
    for key, value in xs.items():
        if value % 2 != 0:
            answer.append(key)
    for key, value in ys.items():
        if value % 2 != 0:
            answer.append(key)

    return answer
