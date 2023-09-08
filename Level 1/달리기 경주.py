'''
선수들의 이름이 1등부터 현재 등수 순서대로 담긴 문자열 배열 players와 해설진이 부른 이름을 담은 문자열 배열 callings가 매개변수로 주어질 때, 
경주가 끝났을 때 선수들의 이름을 1등부터 등수 순서대로 배열에 담아 return 하는 solution 함수를 완성해주세요.
'''

players = ["mumu", "soe", "poe", "kai", "mine"]
callings = ["kai", "kai", "mine", "mine"]

def solution(players, callings):
    answer = []
    player_dic = {}
    order_dic = {}
    
    for i, player in enumerate(players):
        order_dic[i + 1] = player
        player_dic[player] = i + 1

    for player in callings:
        rank = player_dic[player]
        front_player = order_dic[rank -1]

        player_dic[front_player] = rank
        player_dic[player] = rank - 1

        order_dic[rank] = front_player
        order_dic[rank -1] = player


    for player in order_dic.values():
        answer.append(player)

    return answer

print(solution(players, callings))