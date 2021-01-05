import heapq
from queue import PriorityQueue
# 이 문제는 가지치기가 가능하다라는것을 빨리 알아차리는 것이 좋다.
# no가 작업들의 합보다 큰 경우는 배상할 것이 없기 때문에 무조건 0이다.


# 정렬(sort)을 이용해서 풀었을 때
def solution(no, works):
    if no >= sum(works): # 가지치기
        return 0

    # 작업을 해야하는 양만큼 루프를 돌린다.
    for _ in range(no):
        works = sorted(works)
        works[-1] -= 1 # O(no * works log works)

    return sum([i ** 2 for i in works]) # list comprehension


# 힙을 이용해서 풀었을 때
def solution(no, works):
    # 가지치기
    if no > sum(works):
        return 0

    # 파이썬 힙은 최소힙밖에 제공이 안된다.
    # 최대힙을 구하기 위해 -를 붙인다.
    works = [-i for i in works] # max heap
    heapq.heapify(works)

    # 루프를 돌며 정렬을 해보자!
    for _ in range(no):
        # sort : O(n log n) / heappush, heappop : O(log n)
        work = heapq.heappop(works) + 1 # 음수로 바꿔줬으니까 +1이다
        heapq.heappush(works, work) # 값을 더해줌

        # 팝하고 푸시하는 부분을 모듈이 제공하는 기능을 이용해서 풀 수 있다.
        # heappushpop(works, works[0]+1) : 먼저 push하고 pop
        # heapreplace(works, works[0]+1) : 먼저 pop하고 push

    return sum([i**2 for i in works])


# 파라메트릭 서치를 이용해서 풀었을 때
# 60보다 큰 수 중에서 제일 작은 수는 무엇인가?
# 1 5 20 50 80 100 500 <- O(n)만큼 시간 복잡도가 걸린다
# 파라메트릭 서치를 이용하면 O(log n)만큼으로 줄일 수 있다.
def parametric_search(no, works):
    # O(works log works)
    left = 0 # 아무 작업도 안하는 경우 0
    right = 1000 # 각 일에 대한 작업량 최대가 1000이니까

    while left <= right:
        middle = (left + right) // 2
        if no - sum(work - middle for work in works if work > middle):
            left = middle + 1
        else:
            right = middle - 1
    return left


def solution(no, works):
    if no >= sum(works):
        return 0
    pq = PriorityQueue()
    height = parametric_search(no, works)

    for work in works:
        if work > height:
            pq.put(-height) # 역순으로 정렬이 안되기 때문에 -를 붙여서 추가를 해준다.
            no -= work -height
        else:
            pq.put(-work)

    print(height)
    print(no)
    print(pq.queue)

    for _ in range(no):
        # pq.put -> heappush
        # pq.get -> heappop
        pq.put(pq.get() + 1)


# O(n)으로 푸는 법
def solution(no, works):
    counts = [0] * 1001 # 카운트를 세는 배열을 만듬
    max_works = 0 # O(n)

    for work in range(works):
        max_works = max(max_works, work)
        counts[work] += 1

    for i in range(max_works, 0, -1):
        count = min(no, counts[i])
        counts[i] -= count
        counts[i - 1] += count
        no -= count

        if no <= 0:
            break

    return sum([i ** 2 * counts[i] for i in range(max_works + 1)])
