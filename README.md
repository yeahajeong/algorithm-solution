# algorithm-solution

🌳 알고리즘 문제풀이 저장소



---

###### 알고리즘을 잘 공부하는 법

- 항상 **여러가지 풀이 방법**이 있을 수 있다는 것을 염두하기
- 항상 **예외**가 있을 수 있다는 것도 기억하기
- 자잘자잘한 성능보다 **시간복잡도**가 중요! 시간 복잡도를 계산하는데 익숙해지기
- 내 답이 베스트인지 **의심**하기
- 문제를 풀었다면 시행착오 **기록**하기
- 다른 사람의 코드를 많이 보자. 생각하지 못했던 방법을 발견할 수 있다
- 쉽게 포기하지 말되 도저히 모르겠다면 답을 보는 것도 좋은 방법!


###### **어디까지 공부할지** => 문자열처리, 다이나믹 프로그래밍, 이분탐색, BFS, DFS, 백트래킹

###### 파이썬의 장점을 잘 활용하자

- list comprehension (리스트 내포, 리스트 표현식, 지능형 리스트)
- 파이썬만의 오퍼레이터 (**, // 등)
- 파이썬 표준 라이브러리 적극 사용

[이진탐색](#이진탐색)

[정렬](#정렬)

[문자열처리](#문자열처리)



------


### 이진탐색

> - 정렬되어 있는 배열에서 빠르게 특정한 데이터를 찾는 방법
> - **탐색 범위를 절반씩 좁혀가며** 데이터를 탐색
> - 데이터의 개수가 N개일 때 탐색에 필요한 시간 복잡도 O(logN)
> - 탐색 범위가 큰 문제 및 쿼리(Query)를 다루는 문제에 자주 사용
> - 코테에서 이진탐색을 이용해 시간 단축할 수 있는 문제가 많이 출제됨(난이도 상)

```python
# 이진 탐색 소스코드
def binary_search(data, start, end, target):
    while start <= end:
        min = (start + end) // 2
        # 찾은 경우 중간점 인덱스 반환
        if data[mid] == target:
            return mid
        # 중간점의 값보다 큰 경우 오른쪽 확인
        elif data[mid] < target:
            start = mid + 1
        # 중간점의 값보다 작은 경우 왼쪽 확인
        else:
            end = mid - 1
```

#### 💡 파이썬 이진 탐색 라이브러리

```python
from bisect import bisect_left, bisect_right
```

- `bisect_left(a, x)` : 정렬된 순서를 유지하면서 배열 a에 x를 삽입할 가장 왼쪽 위치를 반환
- `bisect_right(a, x)` : 정렬된 순서를 유지하면서 배열 a에 x를 삽입할 가장 오른쪽 위치를 반환

```python
# 값이 [left_value, right_value]인 데이터의 개수를 반환하는 함수
def count_by_range(a, left_value, right_value):
    right_index = bisect_right(a, right_value)
    left_index = bisect_left(a, left_value)
    return right_index - left_index
```

```python
# 정확히 값이 x인 데이터의 인덱스 반환
def index_of_x(a, x):
    i = bisect_left(a, x)
    if i != len(a) and a[i] == x:
        return i
    return None

# x보다 작은 데이터 중에서, 가장 큰 값의 인덱스를 반환
def index_of_less_than_x(a, x):
    i = bisect_left(a, x)
    # x보다 작은 데이터가 존재하는 경우
    if i:
        return i - 1 # 그 중에서 가장 큰 값의 인덱스 반환
    # x가 모든 데이터의 값 이하인 경우 None 반환
    return None

# x보다 작거나 같은 데이터 중에서, 가장 큰 값의 인덱스를 반환
def index_of_less_or_equal_than_x(a, x):
    i = bisect_right(a, x)
    # x보다 작거나 같은 데이터가 존재하는 경우
    if i:
        return i - 1 # 그 중에서 가장 큰 값의 인덱스 반환
    # x가 모든 데이터의 값보다 작은 경우 None 반환
    return None

# x보다 큰 데이터 중에서, 가장 작은 값의 인덱스를 반환
def index_of_greater_than_x(a, x):
    i = bisect_right(a, x)
    # x보다 큰 데이터가 존재하는 경우
    if i != len(a):
        return i # 그 중에서 가장 작은 값의 인덱스 반환
    # x가 모든 데이터의 값 이상인 경우 None 반환
    return None

# x보다 크거나 같은 데이터 중에서, 가장 작은 값의 인덱스를 반환
def index_of_greater_equal_than_x(a, x):
    i = bisect_left(a, x)
    # x보다 크거나 같은 데이터가 존재하는 경우
    if i != len(a):
        return i # 그 중에서 가장 작은 값의 인덱스 반환
    # x가 모든 데이터의 값보다 큰 경우 None 반환
    return None
```

---

### 정렬

> - O(n logn)

```python
list.sort()
```

---

### 스택

> - FIFO : First In Last Out, 먼저 들어온 것이 나중에 나간다

```python
answer.append(1)
answer.append(2)
answer.append(3)
answer.pop() # 3
answer.pop() # 2
answer.pop() # 1
```

---

### 해시

> - Hash는 암호화된 string을 의미
> - Hash Table(Key : value 형태의 자료구조)을 의미
> - 파이썬의 경우 해시 사용이 매우 간단함
> - key 값으로 무엇을 찾아야할 때, 시간을 줄여야 하는 상황에서 많이 사용

```python
answer['a'] = 1
answer['b'] = 2
```

```python
from collection import defaultdic
# defaultdict()은 딕셔너리를 만드는 dict 클래스의 서브 클래스
# defaultdict의 인자로 주어진 객체의 기본값을 딕셔너리의 초기값으로 지정

answer = defaultdict(list)
for i in range(10):
    #defaultdict()의 경우, 키에 해당하는 value를 초기화 시켜주지 않아도 잘 돌아감
    answer[i].append(i)
```

```python
answer = set()
for i in range(10):
    answer.add(i)
for i in range(10):
    if i in answer: 	# answer가 set인 경우 시간복잡도 O(1)
        print(i)		# 만약 answer가 리스트 형태라면 시간복잡도 O(n)
```

#### 💡 파이썬 라이브러리

##### Counter

- hash 혹은 list형 자료의 값 개수를 셀 때 사용
- 딕셔너리 형태로 만들어주고 Counter 객체간 뺄셈 오퍼레이터도 사용이 가능
- O(n)

```python
from collection import Counter

Counter(list) # list의 똑같은 엘리먼트가 몇 개 있는지 딕셔너리 형태로 알려줌
```

---

### BFS 너비우선탐색 & DFS 깊이우선탐색

> - 지도가 있고 옆으로 퍼져나가며 탐색을 진행해야한다? BFS & DFS
> - 완전 탐색이 필요할 경우 DFS 사용
> - BFS 너비 우선 탐색 -> Queue 사용 (선입선출)
> - DFS 깊이 우선 탐색 -> Stack 사용, 재귀호출을 많이 사용 (선입후출)
> - 파이썬 같은 경우 재귀 호출이 상당히 느리기 때문에 가급적 BFS를 사용하는 것이 좋다


#### 💡 파이썬 라이브러리

##### deque

- deque(double-ended queue) : 양방향에서 데이터를 처리할 수 있는 queue

```python
from collections import deque
```

> ##### [ 지원하는 메소드 ]
>
> - append(x) : deque의 우측에 x 추가
> - appendleft(x) : deque의 좌측에 x 추가
> - insert(i, x) : deque의 i번째 위치에 x 추가
> - clear : deque의 모든 요소 삭제
> - pop() : deque의 우측에서 값 하나 추출
> - popleft() : deque의 좌측에서 값 하나 추출
> - remove(value) : deque에서 처음 나타나는 value 삭제

---





#### @ [가사검색](https://programmers.co.kr/learn/courses/30/lessons/60060) `프로그래머스` `Kakao` 

- 이진탐색, 트라이 자료구조
- 난이도 상(Hard)
- [풀이](/solution/가사검색.py)



#### @ [완주하지 못한 선수](https://programmers.co.kr/learn/courses/30/lessons/42576) `프로그래머스`

- 정렬, Counter, 해쉬
- [풀이](/solution/완주하지못한선수.py)
  - 단순 반복으로 풀면 시간 복잡도가 O(n^2)이라 실패함
  - 파이썬 라이브러리를 적극 활용하자!



#### @ [나머지한점]() `프로그래머스`

- Counter
- [풀이](/solution/나머지한점.py)



#### @ [기능개발]() `프로그래머스`

- queue
- [풀이](/solution/기능개발.py)
  - 명확한 의미의 변수명을 사용하자
  - //로 ceil과 같은 효과를 낼 수 있다



#### @ [크레인 인형뽑기 게임](https://programmers.co.kr/learn/courses/30/lessons/64061) `프로그래머스` `Kakao`

- Stack
- [풀이](/solution/크레인인형뽑기게임.py)
  - 확인을 for문 안쪽으로 뒀더니 해결되었다



#### @ [FloodFill](https://school.programmers.co.kr/courses/10515/lessons/67098) `프로그래머스`

- BFS, DFS
- floodfill 알고리즘 : 다차원 [배열](https://ko.wikipedia.org/wiki/배열)에서 지정된 위치와 연결된 부분을 결정하는 알고리즘
- 뭉탱이를 하나로 -> BFS 활용
- 아직 해결 못함



#### @ [단어변환](https://programmers.co.kr/learn/courses/30/lessons/43163#qna) `프로그래머스`

- BFS
- [풀이](/solution/단어변환.py)



#### @[여행경로](https://programmers.co.kr/learn/courses/30/lessons/43164) `프로그래머스`

- DFS
- [풀이]()(/solution/여행경로.py)
  - 테스트 1, 2 런타임 에러



#### @[카펫](https://programmers.co.kr/learn/courses/30/lessons/42842) `프로그래머스`

- 완전탐색
- [풀이](/solution/카펫.py)
  - 다시 풀어본 문제인데 그때랑 풀이방법이 달라졌다.



#### @[베스트앨범](https://programmers.co.kr/learn/courses/30/lessons/42579) `프로그래머스`

- 해시
- [풀이](/solution/베스트앨범.py)
  - 방법을 생각해내는게 어렵다. 흑흑
