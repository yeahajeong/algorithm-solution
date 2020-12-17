"""
생각해보기
x = 가로, y = 세로 (x >= y)
yellow + brown = 전체 크기
x * y = 전체 크기
(x - 1)(y - 1) = yellow
x + y - 1 = brown / 2
"""


def solution1(brown, yellow):
    rec_area = brown + yellow
    height = 3

    while True:
        width = rec_area // height
        if (width - 2) * (height - 2) == yellow:
            return [width, height]
        height += 1


def solution2(brown, yellow):
    total_size = brown + yellow
    row = total_size
    col = row
    while row >= col:
        col = total_size // row # // : 몫 구하는 연산자
        if total_size % row == 0 and row >= col > 2 and (row - 2) * (col - 2) == yellow:
            break
        row -= 1
    return [row, col]


print(solution1(10, 2))
print(solution2(10, 2))