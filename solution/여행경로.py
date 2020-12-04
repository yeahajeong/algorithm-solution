from collections import Counter


def solution(tickets):
    # 딕셔너리 생성 {시작점 : [끝점]}
    routes = dict()
    for (start, end) in tickets:
        routes[start] = routes.get(start, []) + [end]
        # get(key) -> key로 value 얻기
        # key에 해당하는 value가 없을 때는 디폴트 값을 정해둔다. get(key, default)

    # 시작점 : [끝점] 역순 정렬
    for route in routes.keys():
        routes[route].sort(reverse=True)

    # DFS 알고리즘으로 path 만들어줌
    st = ["ICN"]
    path = []

    while st:
        top = st[-1]

        # 루트에 존재하지 않거나 top-key에 대한 값들의 길이가 0일 때 path에 추가
        if top not in routes or len(routes[top]) == 0:
            # 원소가 존재하지 않기 때문에 path에 넣어준다 -> 이때 역순으로 들어가게 됨
            path.append(st.pop())

        # 루트에 존재하고 top-key에 대한 값들의 길이가 1이상일때(=존재할때)
        else:
            # key에 대한 value리스트의 맨 끝을 st에 넣기
            st.append(routes[top][-1])
            routes[top] = routes[top][:-1]
    return path[::-1]


def my_failed_solution(tickets):
    '''
    마지막 목적지를 지정해놓고 풀었더니 변수가 너무 많은 것같다.
    테스트 1, 2에서 런타임 에러가 발생
    '''


    answer = []
    depart_ticket = []

    tickets.sort()

    # 첫 시작이 ICN인 티켓 찾기
    for ticket in tickets:
        if ticket[0] == "ICN":
            depart_ticket.append(ticket)

    # 출발지점
    answer.append(depart_ticket[0][0])
    answer.append(depart_ticket[0][1])
    tickets.remove(depart_ticket[0])

    # 도착지점
    odd_num_city = [k for k, v in Counter(list(y for x in tickets for y in x)).items() if v % 2 == 1]
    print(odd_num_city)
    if len(odd_num_city) > 1 and 'ICN' in odd_num_city:
        odd_num_city.remove('ICN')
    destination = odd_num_city[0]

    while tickets:
        able_tickets = []
        for ticket in tickets:
            if ticket[0] == answer[-1]:
                able_tickets.append(ticket)

        for able_ticket in able_tickets:
            if able_ticket[0][1] == destination:
                able_tickets.remove(able_ticket)

        answer.append(able_tickets[0][1])
        tickets.remove(able_tickets[0])

    return answer


tickets = [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]
tickets2 = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]
tickets3 = [["ICN","BOO"],["ICN","COO"],["COO","ICN"]]


print(solution(tickets3))