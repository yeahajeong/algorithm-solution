def solution(genres, plays):
    answer = []
    genre_play = {}     # {장르 : 총 재생 횟수}
    album = {}   # {장르 : [(재생횟수, 고유번호)]}

    # 해시 만들기
    for i, (genre, play) in enumerate(zip(genres, plays)):
        genre_play[genre] = genre_play.get(genre, 0) + play
        album[genre] = album.get(genre, []) + [(play, i)]

    print("초기 장르:총 재생횟수 딕셔너리 : {}".format(genre_play))
    print("초기 앨범 : {}".format(album))

    # 재생 횟수 내림차순으로 장르별 정렬
    # items() 함수를 사용해 튜플로 만듬
    # x[1]에 총 재생 횟수가 있으니 x[1]을 기준으로 내림차순 정렬
    sorted_genre_play = sorted(genre_play.items(), key=lambda x: x[1], reverse=True)

    print("정렬된 장르: 총재생횟수 딕셔너리 : {}".format(sorted_genre_play))

    # 재생횟수 내림차순 & 인덱스 오름차순
    # -x[0]의 -는 내림차순을 의미
    for genre, total_play in sorted_genre_play:
        print(genre, total_play)
        print("전: {}".format(album))
        album[genre] = sorted(album[genre], key=lambda x: (-x[0], x[1]))
        answer += [index for play, index in album[genre][:2]]
        print("후: {}".format(album))
        print(answer)

    return answer


def fail_solution(genres, plays):
    answer = []

    album = {}
    sorted_album = {}

    # zip과 enumerate 함께 사용하기
    for i, (genre, play) in enumerate(zip(genres, plays)):
        album[genre] = album.get(genre, []) + [[play, i]]
        # temp = []
        # if genre in best_album:
        #     temp = best_album.get(genre)
        # temp.append([play, i])
        # best_album[genre] = temp
        best = genre

    for genre, play_i in album.items():
        sorted_album[genre] = sorted(play_i, key=lambda x: x[0], reverse=True)

    best_album = sorted(sorted_album.items(), key=lambda x: x[0], reverse=True)
    print(best_album)

    for p in best_album:
        answer.append(p[1][0][1])
        answer.append(p[1][1][1])

    # 파이썬에서 dict을 sort/sorted 함수에 넣으면 key를 기준으로 오름차순 정렬함
    # value를 기준으로 정렬하고 싶으면 sorted 함수의 key인자를 이용해 지정해준다.
    # print(best_album)
    # print(sorted(best_album.items(), key=lambda x: x[1], reverse=True))
    return answer


genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]

print(solution(genres, plays))
