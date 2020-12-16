from itertools import combinations
# combination 조합!


def solution(m, weights):
    answer = 0

    for i in range(len(weights)):
        com = combinations(weights, i)
        answer += [sum(candies) for candies in com].count(m)
    return answer