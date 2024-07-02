# 질문마다 판단하는 지표를 담은 1차원 문자열 배열 survey와 검사자가 각 질문마다 선택한 선택지를 담은 1차원 정수 배열 choices가 매개변수로 주어집니다.
# 이때, 검사자의 성격 유형 검사 결과를 지표 번호 순서대로 return 하도록 solution 함수를 완성해주세요.

import unittest


def solution(survey, choices):
    answer = ''
    score_dic = {
        'R': 0, 'T': 0, 'C': 0, 'F': 0, 'J': 0, 'M': 0, 'A': 0, 'N': 0
    }
    type_list = [['R', 'T'], ['C', 'F'], ['J', 'M'], ['A', 'N']]

    for type, score in zip(survey, choices):
        if score < 4:
            score_dic[type[0]] += 4 - score
        elif score > 4:
            score_dic[type[1]] += score - 4

    for types in type_list:
        if score_dic[types[0]] >= score_dic[types[1]]:
            answer += types[0]
        else:
            answer += types[1]

    return answer


class TestSolution(unittest.TestCase):
    def test_solution(self):
        self.assertEqual(solution(["AN", "CF", "MJ", "RT", "NA"], [5, 3, 2, 7, 5]), "TCMA")

    def test_solution2(self):
        self.assertEqual(solution(["TR", "RT", "TR"], [7, 1, 3]), "RCJA")
