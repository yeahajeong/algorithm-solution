# 두 해결책 전부 테스트 2, 5, 28 런타임에러
# 왜인지 모르겠음 다시 풀어볼것,, 지금은 해결책이 떠오르지 않음

from collections import deque


def solution(priorities, location):
    answer = 0
    doc = deque([(v, i) for i, v in enumerate(priorities)])
    best = max(doc)

    while True:
        # 우선 꺼내!
        is_printing = doc.popleft()

        # 더 중요한 문서가 존재하면 맨 뒤로 보냄
        if is_printing[0] < best[0]:
            doc.append(is_printing)
        # 존재하지 않으면 출력을 함
        else:
            answer += 1
            best = max(doc)
            if is_printing[1] == location:
                break

    return answer


def my_solution(priorities, location):
    answer = 0
    wait = len(priorities) - 1
    priorities = deque(priorities)
    prior = max(priorities)

    while True:
        # 우선 꺼내
        move = priorities.popleft()

        # 더 큰것이 존재하면 맨 뒤로 보내야한다.
        if move < prior:
            priorities.append(move)

        # 아니라면 출력
        else:
            answer += 1
            wait -= 1
            prior = max(priorities)

            if location == 0:
                return answer

        if location == 0:
            location = wait
        else:
            location -= 1


def main():
    print(solution([2, 1, 3, 2], 2))
    print("")
    print(solution([1, 1, 9, 1, 1, 1], 0))


if __name__ == '__main__':
    main()
