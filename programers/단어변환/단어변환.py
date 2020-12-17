from collections import deque


# 바꾸기 가능한 단어만 리턴해주는 함수
def can_change(cur_word, words):
    can_change_list = deque()
    for word in words:
        if sum((1 if x != y else 0) for x, y in zip(cur_word, word)) == 1:
            can_change_list.append(word)
    return can_change_list


def solution(begin, target, words):
    answer = 0
    cur_word = begin
    can_change_list = can_change(cur_word, words)

    # 특정 값이 없으면 바로 0반환 - 가지치기
    if target not in words:
        return 0

    # 특정값이 있으면 탐색시작
    else:
        # 한글자만 다른 단어만 담아둔 리스트가 비지 않을 동안 방문
        while can_change_list:
            print(can_change_list)
            answer += 1
            if target in can_change_list:
                break
            else:
                # 바꿔주어야함
                cur_word = can_change_list.popleft()
                words.remove(cur_word)
                can_change_list = can_change(cur_word, words)
    return answer


def fail_my_solution(begin, target, words):
    answer = 0
    compare = begin

    # 특정값이 있는지 확인
    if target not in words:
        return 0

    while words:
        possible =[]
        for word in words:
            if count_same_word(compare, word) == 2:
                possible.append(word)

        # possible에 데이터가 존재한다면(두개 같은 글자가 있다는것)
        if possible:
            answer += 1
            if target in possible:
                break
            else:
                compare = possible[0]
                words.remove(possible[0])
        else:
            break
    return answer


# 두 문자열을 비교해서 같은 문자가 몇개 있는지 반환하는 함수
def count_same_word(w1, w2):
    count = 0
    for i in list(zip(w1, w2)):
        if i[0] == i[1]:
            count += 1
    return count


begin = "hit"
target = "cog"
target2 = "hhh"
words = ["hot", "dot", "dog", "lot", "log", "cog"]
words2 = ["hot", "dot", "dog", "lot", "log"]
words3 = ["hhh", "hht"]

print(solution(begin, target, words))

