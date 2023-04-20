'''
그리워하는 사람의 이름을 담은 문자열 배열 name, 각 사람별 그리움 점수를 담은 정수 배열 yearning, 
각 사진에 찍힌 인물의 이름을 담은 이차원 문자열 배열 photo가 매개변수로 주어질 때, 
사진들의 추억 점수를 photo에 주어진 순서대로 배열에 담아 return하는 solution 함수를 완성해주세요.
'''

def solution(name, yearning, photo):
    answer = []
    score_dic = {}
    
    for nick, score in zip(name, yearning):
        score_dic[nick] = score
    
    for name_list in photo:
        score = 0
        for nick in name_list:
            if nick in score_dic.keys():
                score += score_dic[nick]
        answer.append(score)
    return answer