# 롤케이크에 올려진 토핑들의 번호를 저장한 정수 배열 topping이 매개변수로 주어질 때, 롤케이크를 공평하게 자르는 방법의 수를 return 하도록 solution 함수를 완성해주세요.

import unittest
from collections import defaultdict


def solution(topping):
    answer = 0
    forward = set()
    backward = defaultdict(int)

    for i in topping:
        backward[i] += 1

    for i in topping:
        forward.add(i)
        backward[i] -= 1

        if backward[i] == 0:
            del backward[i]

        if len(forward) == len(backward.keys()):
            answer += 1

    return answer


class TestSolution(unittest.TestCase):
    def test_solution(self):
        self.assertEqual(solution([1, 2, 1, 3, 1, 4, 1, 2]), 2)

    def test_solution2(self):
        self.assertEqual(solution([1, 2, 3, 1, 4]), 0)
