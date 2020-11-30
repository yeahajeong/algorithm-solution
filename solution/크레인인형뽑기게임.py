def solution(board, moves):
    answer = 0
    check = []

    # moves를 하나씩 꺼내서 값을 확인 O(n)
    for move in moves:
        # board 값을 꺼내서 확인 O(n)
        for b in board:
            # move - 1 은 꺼내려는 위치의 인덱스임
            # b[move -1] 의 값이 0이 아닐 경우 임시변수에 담고 그 값을 0으로 바꿔주고 for문에서 탈출
            if b[move - 1] != 0:
                temp = b[move -1]
                b[move - 1] = 0

                check.append(temp) # 체크박스에 꺼낸 인형 추가
                if len(check) > 1 and check[-1] == check[-2] :
                    check.pop()
                    check.pop()
                    answer += 1
                break
    return answer * 2