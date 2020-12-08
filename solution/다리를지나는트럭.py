from collections import deque


def solution(bridge_length, weight, truck_weights):
    time = 1
    total_truck = len(truck_weights)
    truck_weights = deque(truck_weights)
    first = truck_weights.popleft()
    passing = deque(first)
    #
    # while True:
    #     time
    #
    #
    # return time


bridge_length = 2
weight = 10
truck_weights = [7, 4, 5, 6]
print(solution(bridge_length, weight, truck_weights))