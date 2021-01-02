def solution(arrangement):
    answer = 0      # 쇠막대기 조각 변수
    stack = []      # 배열 임시로 담을 스택
    meet = False    # )만났는지 확인 여부

    for arr in arrangement:
        # (를 만날 경우
        if arr == '(':
            # 스택에 저장
            stack.append(arr)
            meet = False
        # )를 만날 경우
        else:
            # 스택에서 꺼냄
            stack.pop()

            # )가 처음으로 나오는경우 : 레이저 쏘기
            if not meet:
                answer += len(stack)
            # )가 연속으로 나오는경우 : 막대기가 끝남
            else:
                answer += 1

            # )를 만났으니 True로 전환
            meet = True

    return answer

# 코드 리뷰
# arrangement 배열에서 ()를 replace로 치환해서 풀면 더 쉽게 풀 수 있다