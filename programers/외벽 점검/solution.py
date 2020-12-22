# 프로그래머스
# 카카오 코딩 테스트
# 외벽 점검 https://programmers.co.kr/learn/courses/10336/lessons/64199

from itertools import permutations


# 완전 탐색 문제
def solution(n, weak, dist):
    # 원형, 시계방향, 반시계방향 문제가 나오면 선형으로 바꿔준다.
    weak_length = len(weak) # 그냥 len(weak)를 사용할 때는 indexError가 발생한다 왜지?
    for i in range(weak_length):
        weak.append(weak[i] + n)

    # 최소값을 찾아야하니까 초기 최소값을 설정
    answer = len(dist) + 1

    # 경우의 수의 각각의 경우마다 할 수 있는 친구들의 순열을 넣어서 찾아본다
    # 처음 for문은 각각 경우의 수
    # 0부터 len(weak) - 1 까지의 위치를 각각 시작점으로 설정
    for start in range(weak_length):

        # 친구를 나열할 수 있는 모든 경우에 대해서 확인
        for friends in list(permutations(dist, len(dist))):
            # 투입할 친구 수
            num_of_friends = 1

            # 해당 친구가 점검할 수 있는 마지막 위치
            position = weak[start] + friends[num_of_friends - 1]

            # 시작점부터 모든 취약한 지점을 확인
            for index in range(start, start + weak_length):

                # index에 위치한 결함을 해결하지 못한 경우
                if position < weak[index]:
                    # 친구를 더 넣어야함
                    num_of_friends += 1

                    # 친구를 넣을 수 없으면 반복문 종료
                    if num_of_friends > len(dist):
                        break

                    # 친구를 넣어줬으니 위치도 변경
                    position = weak[index] + friends[num_of_friends - 1]

            answer = min(answer, num_of_friends)
    # 친구들을 모두 투입해도 취약 지점을 전부 점검할 수 없는 경우에는 -1을 return
    if answer > len(dist):
        return -1
    return answer


print(solution(12, [1, 5, 6, 10], [1, 2, 3, 4]))