# algorithm-solution

🌳 알고리즘 문제풀이 저장소

- 알고리즘을 잘 공부하는 법
  - 항상 **여러가지 풀이 방법**이 있을 수 있다는 것을 염두하기
  - 항상 **예외**가 있을 수 있다는 것도 기억하기
  - 자잘자잘한 성능보다 **시간복잡도**가 중요! 시간 복잡도를 계산하는데 익숙해지기
  - 내 답이 베스트인지 **의심**하기
  - 문제를 풀었다면 시행착오 **기록**하기
  - 다른 사람의 코드를 많이 보자. 생각하지 못했던 방법을 발견할 수 있다
  - 쉽게 포기하지 말되 도저히 모르겠다면 답을 보는 것도 좋은 방법!
- **어디까지 공부할지** => 문자열처리, 다이나믹 프로그래밍, 이분탐색, BFS, DFS, 백트래킹

- 파이썬의 장점을 잘 활용하자
  - list comprehension (리스트 내포, 리스트 표현식, 지능형 리스트)
  - 파이썬만의 오퍼레이터 (**, // 등)
  - 파이썬 표준 라이브러리 적극 사용

[이진탐색](#이진탐색)
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





#### [가사검색](https://programmers.co.kr/learn/courses/30/lessons/60060) `프로그래머스` `Kakao` 

- 이진탐색, 트라이 자료구조
- 난이도 상(Hard)
- [풀이](/solution/가사검색.py)



