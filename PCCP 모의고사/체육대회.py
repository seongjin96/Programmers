'''
당신의 반 학생들의 각 종목에 대한 능력치를 나타내는 2차원 정수 배열 ability가 주어졌을 때, 
선발된 대표들의 해당 종목에 대한 능력치 합의 최대값을 return 하는 solution 함수를 완성하시오.
'''

ability = [[40, 10, 10], [20, 5, 0], [30, 30, 30], [70, 0, 70], [100, 100, 100]]

from itertools import permutations

def solution(ability):
    answer = 0
      
    for all_list in permutations(ability, len(ability[0])):
        total_score = 0
        for i in range(len(ability[0])):
            total_score += all_list[i][i]
                
        answer = max(answer, total_score)
    return answer

print(solution(ability))