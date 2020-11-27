# 풀이 방법이 대표적으로 세가지가 있다.

# 1. 단순 반복으로 푼 풀이 - 효율성에 통과하지 못하는 코드
def solution1(participant, completion):
    for i in completion: # 완주한 선수의 루프를 돈다. O(n)
        if i in participant: # in 문법-> 요소가 있는지 확인하는 문법 (슈가코드, 매직코드 -> 이 로직이 얼마나 걸리는지 모르는게 단점 O(n) )
            participant.remove(i) # 결론적으로 O(n^2) 이기 때문에 시간초과로 효율성이 탈락
    return str(participant[0])
# 시간 복잡도가 O(n^2)으로 느리기 때문에 효율성 테스트에서 실패한다.


# 2. 정렬로 푼 풀이
def solution2(participant, completion):
    # 정렬
    participant.sort() # O(nlogn)
    completion.sort() # O(nlogn)

    print(participant)
    print(completion)

    for p, c in zip(participant, completion): # zip으로 같이 묶는다. O(n)
        # zip은 리스트를 같은 인덱스끼리 잘라서 리스트로 반환을 해준다.
        if p != c: # 만약 다른게 등장하면 완주하지 못한 선수
            return p

    return participant[-1] # 끝까지 없으면 마지막에 있는 것이 완주하지 못한 사람


# 3. Counter를 이용한 풀이 - 파이썬스럽게 푸는 방법
from collections import Counter
# Counter는 hash 혹은 list형 자료의 값 개수를 셀 때 사용한다. 딕셔너리 형태로 만들어주고 Counter 객체간 뺄셈 오퍼레이터도 사용이 가능하다.


def solution3(participant, completion):
    # Counter : 똑같은 엘리먼트가 몇 개 있는지 딕셔너리 형태로 알려줌
    print(Counter(participant))
    print(Counter(completion))
    result = Counter(participant) - Counter(completion) # O(n)
    print(result)
    return list(result.keys())[0]


participant = ["leo", "kiki", "eden"]
completion = ["eden", "kiki"]

participant2 = ["mislav", "stanko", "mislav", "ana"]
completion2 = ["stanko", "ana", "mislav"]

print(solution3(participant,completion))