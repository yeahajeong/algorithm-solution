def solution(prices):
    answer = []
    for index, price in enumerate(prices):
        stack = []
        for n in range(index + 1, len(prices)):
            stack.append(prices[n])
            if price > prices[n]:  # 감소한경우 다음것은 볼 필요도없음!
                break
        answer.append(len(stack))
    return answer


prices1 = [1, 2, 3, 2, 3]
prices = [2, 5, 6, 2, 4, 1]

print(solution(prices)) #[4, 2, 1, 2, 1, 0]