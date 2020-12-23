# 해시 & 스택
# https://school.programmers.co.kr/courses/10515/lessons/67107

'''
코드리뷰
    운송 트럭 문제의 경우 O(names)로 해결이 가능하다.
    while 루프와 pop하는 부분을 제거하고
    if max_weight < weight: 분기 안쪽 고민해 볼것!

    for 루프를 도는 와중에 해당 루프 아이템을 pop하는 것은 위험!
'''


def solution(max_weight, specs, names):
    weight = 0  # 현재의 무게
    specs = dict(specs)  # hash로 변경
    truck = 0

    while len(names) > 0:
        for name in names:
            # 무게를 측정한다.
            weight += int(specs[name])

            # 최대치를 넘으면 트럭에 담으면 안돼!
            if max_weight < weight:
                weight -= int(specs[name])
            # 최대치를 안넘으면 트럭에 담는다. (names에서 삭제)
            else:
                names.pop()
        # 루프가 끝나면 트럭하나 완성
        truck += 1
    return truck


def my_solution(max_weight, specs, names):
    weight = 0  # 현재의 무게
    specs = dict(specs)  # hash로 변경
    truck = 1  # 처음 트럭은 반드시 한 대 존재

    for name in names:
        # name의 무게를 측정한다.
        weight += int(specs[name])

        # 무게가 최대치를 넘으면 트럭에 담으면 안돼! -> 트럭하나를 떠나보내고 새 트럭이 필요
        # 새트럭의 무게는 가장 최근의 name의 무게
        if max_weight < weight:
            weight = int(specs[name])
            truck += 1
    return truck
