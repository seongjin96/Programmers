'''
사과의 최대 점수 k, 한 상자에 들어가는 사과의 수 m, 사과들의 점수 score가 주어졌을 때, 
과일 장수가 얻을 수 있는 최대 이익을 return하는 solution 함수를 완성해주세요.
'''

def solution(k, m, score):
    answer = 0
    score.sort(reverse=True)
    idx = m - 1
    box_len = len(score)
    while(idx < box_len):
        answer += score[idx] * m
        idx += m
    return answer