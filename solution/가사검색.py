# 모든 키워드에 대해 단순히 검사를 한다면 O(NM)으로 시간초과 판정을 받게 됨
# 이 문제는 이진 탐색을 이용해 간단히 해결할 수 있다.

'''
    문제 단순화
    먼저 각 길이에 대해 각각의 리스트를 만들어 단어를 담고 오름차순으로 정렬을 수행
    검색 키워드가 fro?? 일 때 길이가 5인 단어 중에서 ["froaa", "frozz"] 범위에 포함된 단어의 개수를 세면 됨
    count_by_range(a, x)를 이용해 간단히 계산 가능
    접두사에 ? 가 와있으면 리스트에 있는 단어를 뒤집어서 담아주고 오름차순 정렬을 수행
    검색 키워드가 "????o"일 때 길이가 5인 단어 중에서 ["oaaaa", "ozzzz"] 범위에 포함된 단어의 개수를 세면 됨
'''

from bisect import bisect_left, bisect_right


# 값이 [left_value, right_value] 인 데이터의 개수를 반환하는 함수
def count_by_range(a, left_value, right_value):
    right_index = bisect_right(a, right_value)
    left_index = bisect_left(a, left_value)
    return right_index - left_index


# 모든 단어들을 길이마다 나누어서 저장하기 위한 리스트
data = [[] for _ in range(10001)] # 모든 단어의 길이는 만이하라 크기를 설명해줌
# 모든 단어들을 길이마다 나누어서 뒤집어 저장하기 위한 리스트
reversed_data = [[] for _ in range(10001)]


def solution(words, queries):
    answer = []

    # 모든 단어를 접미사 와일드 카드 배열, 접두사 와일드카드 배열에 각각 삽입
    for word in words:
        data[len(word)].append(word)
        reversed_data[len(word)].append(word[::-1]) # 뒤집어서 담기

    # 이진 탐색을 수행하기 위해 각 단어들 정렬 수행
    for i in range(10001):
        data[i].sort()
        reversed_data[i].sort()

    # 쿼리를 하나씩 확인하며 처리
    for q in queries:
        # 접미사에 와일드 카드가 붙은 경우
        if q[0] != '?':
            res = count_by_range(data[len(q)], q.replace('?','a'), q.replace('?', 'z'))
        # 접두사에 와일드 카드가 붙은 경우
        else:
            res = count_by_range(reversed_data[len(q)], q[::-1].replace('?', 'a'), q[::-1].replace('?', 'z'))
        answer.append(res)
    return answer