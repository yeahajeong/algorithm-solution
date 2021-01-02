from itertools import combinations


def leader_solution(n):
    # 에라스토테네스의 체 이용
    # # True -> 소수, False -> 소수아닌 수
    sieve = [True] * n

    # 에라스토테네스의 체를 사용하면 반복을 제곱의 수로 줄일 수 있다.
    # 1은 소수이니까 2부터 시작
    for i in range(2, int(n ** 0.5) + 1):
        # 2부터 시작해서
        if sieve[i]:
            # 그 수의 제곱들을 다 False로 바꿔줌 -> 소수가 아니니까
            for j in range(i * 2, n, i):
                sieve[j] = False

    # True인 애들만 뽑아
    prime_numbers = [i for i in range(2, n) if sieve[i]]

    return [sum(c) for c in combinations(prime_numbers, 3)].count(n)


def solution(n):
    prime_num = prime_num_eratos(n)
    return [sum(i) for i in list(combinations(prime_num, 3))].count(n)


# 에라토스테네스의 체
def prime_num_eratos(n):
    prime_num = [True] * n  # True인 경우는 소수, False인 경우는 소수가 아닌 수
    for i in range(2, int(n ** 0.5) + 1):
        if prime_num[i]:  # i가 소수인 경우 그 수의 배수들은 다 False로 바꿔!
            for j in range(i + i, n, i):
                prime_num[j] = False

    # 소수 꺼내기
    return [i for i in range(2, n) if prime_num[i]]


print(solution(33))