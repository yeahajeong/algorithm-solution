# 빙고 문제는 단순하게 리스트로 하나씩 체크하다보면 시간 초과가 발생해 효율성 테스트를 통과하지 못하는 경우가 생긴다.
# 이 경우 n이 빙고판의 크기라 했을 때 O(n^2 * nums)만큼 시간이 걸린다.
# 그렇기 때문에 입력값인 nums를 Hash로 만들어 O(1)로 체크하는 방식으로 구현하면 O(n^2)으로 구현이 가능하다.
# 해시를 쓰면 O(len(board)^2), 안쓰면 O(len(board)^2 * nums)
def solution(board, nums):
    n = len(board)  # board의 길이
    nums = dict.fromkeys(nums, True)  # nums 리스트의값을 키로 변환해 dict으로 만들어준다.
    row_list = [0] * n
    col_list = [0] * n
    left_diagonal = 0
    right_diagonal = 0

    for i in range(n):  # O(n)
        for j in range(n):  # O(n)
            if board[i][j] in nums:  # O(1)
                board[i][j] = 0
                row_list[i] += 1
                col_list[j] += 1

                if i == j:
                    left_diagonal += 1
                if n - 1 - i == j:
                    right_diagonal += 1
    answer = 0
    answer += sum([1 for i in row_list if i == n])  # 세로
    answer += sum([1 for i in col_list if i == n])  # 가로
    answer += 1 if left_diagonal == n else 0  # 왼쪽 대각선
    answer += 1 if right_diagonal == n else 0  # 오른쪽 대각선

    return answer