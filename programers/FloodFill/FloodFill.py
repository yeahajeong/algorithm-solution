from collections import deque


def solution(n, m, image):
    answer = 0
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    # BFS는 Queue를 이용한 알고리즘

    for sy in range(n):
        for sx in range(m):
            if image[sy][sx] == float('inf'):
                continue
            target_color = image[sy][sx]
            queue = deque[(sy, sx)]  # 처음 선택된 좌표

            while queue:
                y, x = queue.popleft()  # list의 pop은 O(n)

                for dy, dx in directions:
                    py = y + dy
                    px = x + dx
                    if px >= m or px < 0 or py >= n or py < 0:
                        continue
                    if image[py][px] == target_color:
                        image[py][px] = float('inf')
                        queue.append((py, px))
            answer += 1
        return answer


image = [[1, 2, 3], [3, 2, 1]]
print(solution(2, 3, image))
