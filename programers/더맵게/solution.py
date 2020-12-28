from heapq import heapify, heappush, heappop
# 자료구조 Heap을 사용해서 풀 수 있다.
# 완전 힙을 위한 문제이니까 이런 문제가 나오면 무조건 힙을 사용하는것으로 외우도록 하자!


# 정렬로 풀었을 때
def solution1(scoville, K):
    scoville.sort() # O(n log n)
    count = 0

    while scoville[0] < K:
        food1 = scoville.pop(0)
        if len(scoville) == 0: # try except로 바꿔서 하는것이 좋다!
            return -1
        food2 = scoville.pop(0)
        scoville.append(food1 + food2 * 2)
        scoville.sort()
        count += 1


# 힙으로 푼 방법
def solution2(scoville, K):
    heapify(scoville)
    count = 0

    while scoville[0] < K:
        # (추천)EAFP 허락을 구하는 것보다 용서를 구하는 것이 쉽다. : 일단 하고 문제가 생기면 나중에 처리하는 방식
        # LBYL 누울자리를 보고 다리를 뻗어라 : 코드를 실행하기 전에 if로 체크하는 방식
        try:
            heappush(scoville, heappop(scoville) + heappop(scoville) * 2)
        except IndexError:
            return -1
        count += 1
    return count