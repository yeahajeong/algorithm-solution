# 쇠막대기는 전형적인 스택 문제이다. () 바로 닫히는 괄호를 replace로 변형해서 풀어주면 더 깔끔해짐
def solution(arrangement):
    answer = 0
    stack = 0 # stack의 길이만 체크하기 때문에 정수형 변수로 관리해도 괜찮다

    # 꿀팁 : ()이면 레이저니까 다른 문자로 대체하면 인덱스를 구할 필요가없다.
    for paren in arrangement.replace('()', '|'):
        if paren == '(': # 쇠막대기의 시작
            stack += 1 # 스택의 길이가 하나 늘었다는 의미
        elif paren == '|': # 레이저 발사
            pass
        else: # 쇠막대기의 끝
            stack -= 1
            answer += 1 # 닫히면 쇠막대기가 하나 추가되기 때문

    return answer
