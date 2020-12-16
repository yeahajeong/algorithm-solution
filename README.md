

# algorithm-solution

🌱 코딩테스트 풀이 저장소

🌱 자료구조, 알고리즘 정리

---

###### ✍ 알고리즘을 잘 공부하는 법

- 항상 **여러가지 풀이 방법**이 있을 수 있다는 것을 염두하기
- 항상 **예외**가 있을 수 있다는 것도 기억하기
- 자잘자잘한 성능보다 **시간복잡도**가 중요! 시간 복잡도를 계산하는데 익숙해지기
- 내 답이 베스트인지 **의심**하기
- 문제를 풀었다면 시행착오 **기록**하기
- 다른 사람의 코드를 많이 보자. 생각하지 못했던 방법을 발견할 수 있다
- 쉽게 포기하지 말되 도저히 모르겠다면 답을 보는 것도 좋은 방법!

###### ✍ 파이썬의 장점을 잘 활용하자

- list comprehension (리스트 내포, 리스트 표현식, 지능형 리스트)
- 파이썬만의 오퍼레이터 (**, // 등)
- 파이썬 표준 라이브러리 적극 사용

###### **✍ 어디까지 공부할지** (코딩테스트에 많이 나오는 문제 위주)

- 문자열 처리
- DF (다이나믹 프로그래밍)
- 이분탐색
- BFS, DFS
- 백트래킹

---

## ✔ 문자열 처리

#### 🔍 문자열 길이

```python
len(문자열)
```

#### 🔍 특정문자 개수 찾기

```python
s.count('찾을 문자')
```

#### 🔍 문자 인덱스 반환

```python
s.find('찾을 문자')		# 존재하지 않는다면 -1 반환
s.index('찾을 문자')	# 존재하지 않는다면 오류 발생
```

#### 🔍 문자열 사이에 문자 삽입하기 - join

```python
"삽입할 문자".join('문자열')
```

#### 🔍 소 ↔ 대 문자 변경

```python
s.upper()	# 소 -> 대
s.lower() 	# 대 -> 소
```

#### 🔍 글자 치환

```python
s.replace('대체문자(열)', '기존문자(열)')
```

#### 🔍 기준으로 글자 쪼개기

```python
s.split(기준)
```

#### 🔍 문자열 개수 단위로 쪼개기

```python
splited = [s[i:i+size] for i in range(0, LENGTH, size)]
# size = 3 : aabbaccc -> ['aab', 'bac', 'cc']
```

---

## ✔ 2차 리스트

#### 🔍 초기화 m * n 행렬

```python
board = [[0] * n for i in range(m)]
```

#### 🔍 행열 뒤집기 (n*m)

```python
reversed = list(map(list,zip(*board)))
```

#### 🔍 90도 회전

```python
def rotate90(arr):
    return list(zip(*arr[::-1]))
```

---

## ✔ stack - 스택

- 파이썬에서는 리스트로 구현
- FIFO : First In Last Out, 먼저 들어온 것이 나중에 나간다.

---

## ✔ dictionary - 해시

- Hash Table (`key` : `value` 형태의 자료구조)를 의미
- `key` 값에는 변하지 않는 값만 가능 (리스트 불가, 튜플 가능)
- key 값으로 무엇을 찾아야할 때, 시간을 줄여야 하는 상황에서 많이 사용

#### 🔍 빈 딕셔너리 생성

```python
d = {}
d = dic()
```

#### 🔍 요소가 있는 딕셔너리 생성

```python
d = {key:value ...}
```

#### 🔍 요소 추가

```python
d[key] = value
```

#### 🔍 요소 삭제

```python
del d[key]
d.pop(key, default)		# 해당 값이 없으면 디폴트 값 리턴
d.clear()				# 모두 삭제
```

#### 🔍 get

```python
d[key]					# 해당 값이 없으면 오류발생
d.get(key)  			# 해당 값이 없으면 None
d.get(key, default)  	# 해당 값이 없으면 미리정해둔 디폴트값을 대신 가져옴
```

#### 🔍 key 값만 얻기

```python
d.keys()	# 객체로 반환
```

#### 🔍 value 값만 얻기

```python
d.values()	# 객체로 반환
```

#### 🔍 딕셔너리 모든 값 얻기

```python
d.items()	# 튜플로 묶어 객체로 반환
```

#### 🔍 존재 확인 -> True, False 반환

```python
key in a
```

📁 Link - [defaultdict](#defaultdic - collections)

📁 Link - [Counter](#Counter - collections)

---

## ✔ heap - 힙

```python
import heapq
```

- 최댓값과 최솟값을 빠르게 찾기 위한 자료구조
- 파이썬의 힙은 최소힙을 제공
- 시간복잡도 - O(log N)

#### 🔍 원소 추가 - O(log N)

```python
list = []
heapq.heappush(list, value)
```

#### 🔍 원소가 있는 list를 heap으로 변환 - O(N)

```python
heapq.heapify(list)
```

#### 🔍 가장 작은 원소 반환 -> 그 다음 작은 원소가 루트로 올라옴 - O(log N)

```python
heapq.heappop(list)
```

#### 🔍 원소를 삭제하지 않고 최소값 반환

```python
list[0]
```

#### 🔍 [응용] 최대힙

힙에 튜플을 원소로 추가하거나 삭제하면 튜플 내에서 맨 앞에 있는 값을 기준으로 최소 힙이 구성되는 원리를 이용, 각 값에 대한 우선 순위를 구한 후, (우선순위, 값) 구조의 튜플을 힙에 추가하거나 삭제

힙에서 값을 읽어올 때는 각 튜플에서 인덱스 1에 있는 값을 취하면 된다(우선순위에는 관심이 없으므로)

```python
import heapq

for num in nums:
  heapq.heappush(heap, (-num, num))  # (우선 순위, 값)

while heap:
  print(heapq.heappop(heap)[1])  # index 1
```

#### 🔍 [응용] K번째 최소값 / 최대값

```python
import heapq

# K번째 최소값
def kth_smallest(nums, k):
    list = []
    for num in nums:
        heapq.heappush(list, num)

    kth_min = None
    for _ in range(k):
        kth_min = heapq.heappop(list)
    return kth_min
```

#### 🔍 [응용] 힙 정렬 알고리즘

```python
import heapq

def heap_sort(nums):
    heap = []
    for num in nums:
        heapq.heappush(heap, num)
  
	sorted_nums = []
    while heap:
        sorted_nums.append(heapq.heappop(heap))
    return sorted_nums
```

---

## ✔ BFS, DFS - 너비우선탐색, 깊이우선탐색

- 지도가 있고 옆으로 퍼져나가며 탐색을 진행해야한다? BFS & DFS
- 완전 탐색이 필요할 경우 DFS 사용
- BFS 너비 우선 탐색 -> Queue 사용 (선입선출)
- DFS 깊이 우선 탐색 -> Stack 사용, 재귀호출을 많이 사용 (선입후출)
- 파이썬 같은 경우 재귀 호출이 상당히 느리기 때문에 가급적 BFS를 사용하는 것이 좋다

📁 Link - [BFS - deque](#deque)

---

## ✔ 이진 탐색

- 정렬되어 있는 배열에서 빠르게 특정한 데이터를 찾는 방법
- **탐색 범위를 절반씩 좁혀가며** 데이터를 탐색
- 데이터의 개수가 N개일 때 탐색에 필요한 시간 복잡도 O(logN)
- 탐색 범위가 큰 문제 및 쿼리(Query)를 다루는 문제에 자주 사용
- 코테에서 이진탐색을 이용해 시간 단축할 수 있는 문제가 많이 출제됨(난이도 상)

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

📁 Link - [이진탐색 라이브러리]()

---

## ✔ math

```python
import math
```

#### 🔍 ceil - 올림

```python
math.ceil(num / div)
```

#### 🔍 factorial

```python
math.factorial(3)
```

---

## ✔ itertools

```python
import itertools
```

#### 🔍 permutations - 순열

```python
from itertools import permutations

permutations(range(1, 10), 3)
permutations(lst)
```

#### 🔍 combinations - 조합

```python
from itertools import combinations

combinations('ABC', 2)
```

#### 🔍 product - 중복 순열

```python
from itertools import product

product(range(1,n1+1), range(1,n2+1), range(1,n3+1))

or_not = [(0, 500), (0, 1500)]
list(product(*or_not))

#[(0,0), (0,1500), (500,0), (500,1500)]
```

#### 🔍 chain - flatten(2차 리스트 -> 1차 리스트)

```python
from itertools import chain

itertools.chain(*board)
chain(*board)
```

---

## ✔ defaultdic - collections

```python
from collections import defaultdict

# 딕셔너리를 만드는 dict 클래스의 서브클래스이다. 
# 인자로 주어진 객체의 기본값을 딕셔너리의 초기값으로 지정
# defaultdict()의 경우, 키에 해당하는 value를 초기화 시켜주지 않아도 잘 돌아감

dict_list = defaultdict(list)	# 시간 복잡도 O(n)
dict_set = defaultdict(set)		# 시간 복잡도 O(1)
dict_int = defaultdict(int) 	# -> 0으로 셋팅

for i in range(10):
    answer[i].append(i)
```

## ✔ Counter - collections

```python
from collection import Counter

Counter(list) # list의 똑같은 엘리먼트가 몇 개 있는지 딕셔너리 형태로 알려줌
```

- hash 혹은 list형 자료의 값 개수를 셀 때 사용
- 딕셔너리 형태로 반환을 해주고 Counter 객체간 뺄셈 오퍼레이터도 사용이 가능
- 시간 복잡도 - O(n)

## ✔ deque - collections

```python
from collections import deque
```

- 양방향에서 데이터를 처리할 수 있는 queue

#### 🔍 요소 추가

```python
dq.append(x)		# 우측에 x 추가
dq.appendleft(x)	# 좌측에 x 추가
dq.insert(i, x)		# i번째 위치에 x 추가
```

#### 🔍 요소 삭제

```python
dq.pop()		# 우측에서 값 하나 추출
dq.popleft()	# 좌측에서 값 하나 추출
dq.clear()		# deque의 모든 요소 삭제
dq.remove(x)	# 처음 나타나는 x값 삭제
```

#### 🔍 요소 조회

```python
dq[0]
```

---

## ✔ bisect

```python
from bisect import bisect_left, bisect_right
```

#### 🔍 정렬된 순서를 유지하면서 리스트에 x를 삽입할 가장 왼쪽 위치 반환

```python
bisect_left(list, x)
```

#### 🔍 정렬된 순서를 유지하면서 리스트에 x를 삽입할 가장 오른쪽 위치 반환

```python
bisect_right(list, x)
```

#### 🔍 값이 [left_value, right_value]인 데이터의 개수를 반환하는 함수

```python
def count_by_range(a, left_value, right_value):
    right_index = bisect_right(a, right_value)
    left_index = bisect_left(a, left_value)
    return right_index - left_index
```

#### 🔍 값이 정확이 x인 데이터의 인덱스 반환

```python
def index_of_x(a, x):
    i = bisect_left(a, x)
    if i != len(a) and a[i] == x:
        return i
    return None
```

#### 🔍 x보다 작은 데이터 중에서, 가장 큰 값의 인덱스를 반환

```python
def index_of_less_than_x(a, x):
    i = bisect_left(a, x)
    # x보다 작은 데이터가 존재하는 경우
    if i:
        return i - 1 # 그 중에서 가장 큰 값의 인덱스 반환
    # x가 모든 데이터의 값 이하인 경우 None 반환
    return None
```

#### 🔍 x보다 작거나 같은 데이터 중에서, 가장 큰 값의 인덱스를 반환

```python
def index_of_less_or_equal_than_x(a, x):
    i = bisect_right(a, x)
    # x보다 작거나 같은 데이터가 존재하는 경우
    if i:
        return i - 1 # 그 중에서 가장 큰 값의 인덱스 반환
    # x가 모든 데이터의 값보다 작은 경우 None 반환
    return None
```

#### 🔍 x보다 큰 데이터 중에서, 가장 작은 값의 인덱스를 반환

```python
def index_of_greater_than_x(a, x):
    i = bisect_right(a, x)
    # x보다 큰 데이터가 존재하는 경우
    if i != len(a):
        return i # 그 중에서 가장 작은 값의 인덱스 반환
    # x가 모든 데이터의 값 이상인 경우 None 반환
    return None
```

#### 🔍 x보다 크거나 같은 데이터 중에서, 가장 작은 값의 인덱스를 반환

```python
def index_of_greater_equal_than_x(a, x):
    i = bisect_left(a, x)
    # x보다 크거나 같은 데이터가 존재하는 경우
    if i != len(a):
        return i # 그 중에서 가장 작은 값의 인덱스 반환
    # x가 모든 데이터의 값보다 큰 경우 None 반환
    return None
```

------

## ⏳ 시간 복잡도 정리

#### 💡 List 시간복잡도

| Operation     | Example        | Big-O       | Notes                       |
| ------------- | -------------- | ----------- | --------------------------- |
| Index         | I[i]           | O(1)        |                             |
| Store         | l[i] * 0       | O(1)        |                             |
| Length        | len(l)         | O(1)        |                             |
| Append        | l.append(5)    | O(1)        |                             |
| Pop           | l.pop()        | O(1)        | l.pop(-1)과 동일            |
| Clear         | l.clear()      | O(1)        | ㅣ = [] 와 유사             |
| Slice         | l[a:b]         | O(b-a)      | ㅣ[:] : O(len(????)) = O(N) |
| Extend        | l.extend(...)  | O(len(...)) | 확장 길이에 따라            |
| Construction  | list(...)      | O(len(...)) | 요소 길이에 따라            |
| check ==, !=  | l1 == l2       | O(N)        | 비교                        |
| Insert        | l.insert(i, v) | O(N)        | i 위치에 v 추가             |
| Delete        | del l[i]       | O(N)        |                             |
| Remove        | l.remove(...)  | O(N)        |                             |
| Containment   | x in/not in l  | O(N)        | 검색                        |
| Copy          | l.copy()       | O(N)        | l[:] 과 동일 - O(N)         |
| Pop           | l.pop(i)       | O(N)        | l.pop(0) : O(N)             |
| Extreme value | min(l)/max(l)  | O(N)        | 검색                        |
| Reverse       | l.reverse()    | O(N)        | 그대로 반대로               |
| Iteration     | for v in l:    | O(N)        |                             |
| Sort          | l.sort()       | O(N log N)  |                             |
| Multiply      | k * l          | O(k N)      | l * len(l) = O(N**2)        |

#### 💡 Dict 시간복잡도

| Operation        | Example     | Big-O       | Notes                   |
| ---------------- | ----------- | ----------- | ----------------------- |
| Index            | d[k]        | O(1)        |                         |
| Store            | d[k] = v    | O(1)        |                         |
| Length           | len(d)      | O(1)        |                         |
| Delete           | dle d[k]    | O(1)        |                         |
| get / setdefault | d.method    | O(1)        |                         |
| Pop              | d.pop(k)    | O(1)        |                         |
| Pop item         | d.popitem() | O(1)        |                         |
| Clear            | d.clear()   | O(1)        | s ={} or dict() 과 유사 |
| View             | d.keys()    | O(1)        | d.values() 와 동일      |
| Construction     | dict(...)   | O(len(...)) |                         |
| Iteration        | for k in d: | O(N)        |                         |

---

## 🐣 코테 문제 풀이

#### 1. [가사검색](https://programmers.co.kr/learn/courses/30/lessons/60060) `프로그래머스` `Kakao` 

- 이진탐색, 트라이 자료구조
- 난이도 상(Hard)
- [풀이](/solution/가사검색.py)



#### 2. [완주하지 못한 선수](https://programmers.co.kr/learn/courses/30/lessons/42576) `프로그래머스`

- 정렬, Counter, 해쉬
- [풀이](/solution/완주하지못한선수.py)
  - 단순 반복으로 풀면 시간 복잡도가 O(n^2)이라 실패함
  - 파이썬 라이브러리를 적극 활용하자!



#### 3. [나머지한점]() `프로그래머스`

- Counter
- [풀이](/solution/나머지한점.py)



#### 4. [기능개발]() `프로그래머스`

- queue
- [풀이](/solution/기능개발.py)
  - 명확한 의미의 변수명을 사용하자
  - //로 ceil과 같은 효과를 낼 수 있다



#### 5. [크레인 인형뽑기 게임](https://programmers.co.kr/learn/courses/30/lessons/64061) `프로그래머스` `Kakao`

- Stack
- [풀이](/solution/크레인인형뽑기게임.py)
  - 확인을 for문 안쪽으로 뒀더니 해결되었다



#### 6. [FloodFill](https://school.programmers.co.kr/courses/10515/lessons/67098) `프로그래머스` 🤬

- BFS, DFS
- floodfill 알고리즘 : 다차원 [배열](https://ko.wikipedia.org/wiki/배열)에서 지정된 위치와 연결된 부분을 결정하는 알고리즘
- 뭉탱이를 하나로 -> BFS 활용
- 아직 해결 못함



#### 7. [단어변환](https://programmers.co.kr/learn/courses/30/lessons/43163#qna) `프로그래머스`

- BFS
- [풀이](/solution/단어변환.py)



#### 8. [여행경로](https://programmers.co.kr/learn/courses/30/lessons/43164) `프로그래머스` 🤢

- DFS
- [풀이]()(/solution/여행경로.py)
  - 테스트 1, 2 런타임 에러



#### 9. [카펫](https://programmers.co.kr/learn/courses/30/lessons/42842) `프로그래머스`

- 완전탐색
- [풀이](/solution/카펫.py)
  - 다시 풀어본 문제인데 그때랑 다르게 풀었네..



#### 10. [베스트앨범](https://programmers.co.kr/learn/courses/30/lessons/42579) `프로그래머스` 🤢

- 해시
- [풀이](/solution/베스트앨범.py)
  - 방법을 생각해내는게 어렵다. 흑흑
  - 딕셔너리(해시) 사용법에 대해 익숙하지 않아서 반복해서 풀고 기억하자



#### 11. [다리를 지나는 트럭 ](https://programmers.co.kr/learn/courses/30/lessons/42583) `프로그래머스` 🤢

- 큐
- [풀이](/solution/다리를지나는트럭.py)
  - 해결하지 못함. 해결방법을 떠올릴 수 없음
- [다른사람풀이](/solution/다리를지나는트럭(다른사람풀이).py)



#### 12. [디스크 컨트롤러](https://programmers.co.kr/learn/courses/30/lessons/42627) `프로그래머스`🤬

- 힙(Heap)
- [풀이](/solution/디스크컨트롤러.py)



#### 13. [주식가격](https://programmers.co.kr/learn/courses/30/lessons/42584) `프로그래머스`

- 스택
- [풀이](/solution/주식가격.py)
  - 테스트케이스를 잘못잡아서 더 오래걸렸다.



#### 14. [프린터](https://programmers.co.kr/learn/courses/30/lessons/42587) `프로그래머스 `🤬

- 스택 / 큐
- [풀이](/solution/프린터.py)
