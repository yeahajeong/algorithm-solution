import heapq


def solution(scoville, K):
    answer = 0

    while scoville[0] < K:
        scoville.sort()

        # 정확성 테스트를 위해 이 부분을 예외 처리를 해주어야한다.
        # 배열의 첫번째 두번째가 존재해야함...
        try:
            new_scoville = scoville[0] + (scoville[1]*2)
            del scoville[0:2]
        except IndexError as e:
            break

        # print("스코빌: {}".format(scoville))
        scoville.append(new_scoville)
        answer += 1

    if len(scoville) < 1 or scoville[0] < K:
        return -1

    return answer


# heap을 사용한 풀이
def heapsolution(scoville, K):
    answer = 0

    # 이 부분은 지우는 것이 좋다
    # heapq.heapify(scoville)
    # print(scoville)

    while scoville[0] < K:
        try:
            heapq.heappush(scoville, heapq.heappop(scoville) + (heapq.heappop(scoville)*2))
            answer += 1
        except IndexError:
            return -1

    return answer