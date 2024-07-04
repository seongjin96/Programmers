# 전화번호부에 적힌 전화번호를 담은 배열 phone_book 이 solution 함수의 매개변수로 주어질 때,
# 어떤 번호가 다른 번호의 접두어인 경우가 있으면 false를 그렇지 않으면 true를 return 하도록 solution 함수를 작성해주세요.

import unittest


def solution(phone_book):
    dic = dict()
    for phone in phone_book:
        for i in range(1, len(phone)):
            dic[phone[:i]] = 1

    for phone in phone_book:
        if phone in dic:
            return False

    return True


class Test(unittest.TestCase):
    def test_solution(self):
        self.assertFalse(solution(["119", "97674223", "1195524421"]))

    def test_solution2(self):
        self.assertTrue(solution(["123", "456", "789"]))

    def test_solution3(self):
        self.assertFalse(solution(["12", "123", "1235", "567", "88"]))
