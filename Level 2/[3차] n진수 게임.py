# 이진수로 진행하는 게임에 익숙해져 질려가던 사람들은 좀 더 난이도를 높이기 위해 이진법에서 십육진법까지 모든 진법으로 게임을 진행해보기로 했다.
# 숫자 게임이 익숙하지 않은 튜브는 게임에 져서 벌칙을 받는 굴욕을 피하기 위해,
# 자신이 말해야 하는 숫자를 스마트폰에 미리 출력해주는 프로그램을 만들려고 한다. 튜브의 프로그램을 구현하라.

import unittest


def calculate_base(n, base):
    hex_dict = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    rev_base = ''

    while n > 0:
        n, mod = divmod(n, base)
        if mod in hex_dict.keys():
            rev_base += str(hex_dict[mod])
        else:
            rev_base += str(mod)

    return rev_base[::-1]


def solution(n, t, m, p):
    answer = ''
    total_num = '0'
    for num in range(1, t * m):
        total_num += calculate_base(num, n)

    for i in range(p-1, t * m, m):
        answer += total_num[i]

    return answer


class TestSolution(unittest.TestCase):
    def test_solution(self):
        self.assertEqual(solution(2, 4, 2, 1), "0111")

    def test_solution2(self):
        self.assertEqual(solution(16, 16, 2, 1), "02468ACE11111111")

    def test_solution3(self):
        self.assertEqual(solution(16, 16, 2, 2), "13579BDF01234567")
