from collections import deque


def solution(bridge_length, weight, truck_weights):
    # 대기 중인 트럭들 뒤집어 주기
    # pop(0)하면 효율적이지 않기 때문
    truck_weights = truck_weights[::-1]

    # 각 트럭이 다리에 오른 후 시간이 얼마나 흘렸는지 나타내기 위한 리스트
    passing = deque([0] * bridge_length)
    time = 0
    print(passing)

    while passing:
        time += 1
        passing.popleft()
        print("현재시간 : {}".format(time))

        if truck_weights:
            if sum(passing) + truck_weights[-1] <= weight:
                passing.append(truck_weights.pop())
            else:
                passing.append(0)
        print(passing)
    return time


def my_solution(bridge_length, weight, truck_weights):
    time = 1                        # 시간
    trucks = deque(truck_weights)   # 큐에 담기
    wait = trucks.popleft()         # 대기 트럭

    # 다리위에 올리기
    passing = deque()
    passing.append([wait, 1])
    cum_weight = wait

    print("초기화된 값들 확인")
    print("trucks : {}".format(trucks))
    print("대기 트럭 : {}".format(wait))
    print("다리를 지나가고있는 트럭 : {}".format(passing))
    print("")

    while True:
        # 시간 경과
        time += 1
        for tt in passing:
            tt[1] += 1
        print("현재 시간 : {}".format(time))
        print("현재 다리 상황 : {}".format(passing))

        # 다리를 다 건넌 트럭이 있는지 확인
        print("다리를 다 건넌 트럭이 있는지 확인")
        for passing_truck in passing:
            print("passing_truck : {}".format(passing_truck))
            print("passing_truck[1] : {}".format(passing_truck[1]))
            # 있으면 제거, 무게도 조절
            if passing_truck[1] > bridge_length:
                print("다리를 다 건넌 트럭이 있어서 제거한다!")
                done = passing.popleft()
                cum_weight -= done[0]
        print("확인 후 다리 상황: {}".format(passing))
        print("다리 위 무게 : {}".format(cum_weight))

        # 대기 트럭 확인
        if len(trucks) > 0:
            print("아직 대기 중인 트럭이 있으니 대기 중 트럭 변경")
            wait = trucks.popleft()
        # 대기 트럭이 없으면 대기트럭에 None 저장
        else:
            print("더이상 지나갈 트럭이 있지 않음")
            wait = False
        print("현재 대기 트럭 : {}".format(wait))

        # 다리 위에 아무 트럭도 없거나 무게를 초과하지 않으면 위에 대기 트럭을 올려준다.
        if wait and (len(passing) == 0 or sum(t[0] for t in passing) + wait <= weight):
            print("트럭을 올립니다.")
            passing.append([wait, 1])
            cum_weight += wait[0]

        if wait==False and len(passing) == 0:
            break

        print("")


bridge_length = 2
weight = 10
truck_weights = [7, 4, 5, 6]
print(solution(bridge_length, weight, truck_weights))