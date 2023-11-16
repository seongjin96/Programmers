'''
노래를 수록하는 기준은 다음과 같습니다.

1. 속한 노래가 많이 재생된 장르를 먼저 수록합니다.
2. 장르 내에서 많이 재생된 노래를 먼저 수록합니다.
3. 장르 내에서 재생 횟수가 같은 노래 중에서는 고유 번호가 낮은 노래를 먼저 수록합니다.

노래의 장르를 나타내는 문자열 배열 genres와 노래별 재생 횟수를 나타내는 정수 배열 plays가 주어질 때, 
베스트 앨범에 들어갈 노래의 고유 번호를 순서대로 return 하도록 solution 함수를 완성하세요.
'''

genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]

from collections import defaultdict

def solution(genres, plays):
    answer = []
    # 장르별 총 재생 횟수
    total_play = defaultdict(int)
    # 고유번호별 재생 횟수
    unique_num = defaultdict(list)

    for i in range(len(genres)):
        total_play[genres[i]] += plays[i]
        unique_num[genres[i]].append([i, plays[i]])
    
    # 속한 노래가 많이 재생된 장르 순으로 정렬
    sorted_play = sorted(total_play.items(), key=lambda x: x[1], reverse=True)

    for genre, play in sorted_play:
        play_list = unique_num[genre]
        # 장르 내에서 많이 재생 된 순으로 정렬
        # 재생 횟수가 같을 경우 고유 번호가 낮은 순으로 정렬
        play_list.sort(key=lambda x:(-x[1], x[0]))
        
        for i in range(len(play_list)):
            # 최대 2곡까지만 저장
            if i == 2:
                break
            answer.append(play_list[i][0])
        
    return answer

print(solution(genres, plays))