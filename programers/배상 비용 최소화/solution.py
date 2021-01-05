# Heap, 파라메트릭서치
# 배상 비용 최소화의 경우 제곱수를 줄이는 것이 가장 최선이기 때문에 항상 정렬된 첫 번째 요소를 선택해야 합니다.
# Heap이 아닌 정렬로도 가능하지만 매번 정렬하면 O(n log n)을 n번 만큼 돌리게 되어 O(n^2 log n) 만큼 시간이 소요됩니다.
# 반면 Heap은 최초에 한 번 O(n log n) 정렬이 실행되고
# 그 이후에 요소가 추가되거나 삭제될 때는 O(log n)만큼 시간이 소요되기 때문에 정렬보다 유리합니다.
# 단, 파이썬의 sort는 Tim sort라는 특이한 알고리즘으로 실행되어
# Heap으로 풀때와 유사하거나 아주 조금 더 느리게 동작합니다. 그래서 효율성 테스트를 통과할 수 있습니다.
import heapq


# no 작업할 수 있는 시간 works 선박별로 남은 일의 작업량
# no가 works의 합보다 크다면 무조건 0이다.
def solution(no, works):
    if no > sum(works):
        return 0
    else:
        result = 0

        # no를 하나씩 줄여나가는 것보다 for in range를 사용!
        # 제일 큰 수를 일해야지 비용이 최소화가 된다. -> 큰 수를 깎아야함
        for _ in range(no):  # 인덱스가 필요없을 때 _를 사용한다.
            works.sort()
            works[-1] -= 1

        # list comprehension을 사용해서 줄일 수 있다.
        # for n, i in enumerate(works):
        #     works[n] = i*i

        return sum([i ** 2 for i in works])


def pqsolution(no, works):
    if no > sum(works):
        return 0
    else:
        # 큰 값이 우선 순위가 높아야하니까 -를 붙여서 우선순위를 담는다.
        works = [(-i, i) for i in works]
        heapq.heapify(works) # 힙으로 만들기 (우선순위에 따라 정렬됨)
        # print("우선순위 큐: {}".format(works))

        for _ in range(no):
            # 제일 큰 값이 루트에 있으니 꺼냄
            # 루트 꺼내서 우선순위 말고 값 -1을 해준다.
            work = heapq.heappop(works)[1] - 1

            # 일을 한 후 다시 우선순위 큐에 저장
            heapq.heappush(works, (-work, work))

        return sum(i[1] ** 2 for i in works)

# no = 3
# works = [4, 3, 3]
# works2 = [3, 3, 3]
# print(pqsolution(no, works))