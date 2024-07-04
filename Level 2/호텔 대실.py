# 예약 시각이 문자열 형태로 담긴 2차원 배열 book_time이 매개변수로 주어질 때,
# 코니에게 필요한 최소 객실의 수를 return 하는 solution 함수를 완성해주세요.

## 누적합 사용

import unittest
from collections import defaultdict


def solution(book_time):

    def get_time(time):
        HH, MM = map(int, time.split(':'))
        return HH * 60 + MM

    MAX, now, books = 0, 0, defaultdict(int)

    for time in book_time:
        start_time, end_time = get_time(time[0]), get_time(time[1])
        books[start_time] += 1
        books[end_time + 10] -= 1

    books = sorted(list(map(list, books.items())))

    for book in books:
        now += book[1]
        MAX = max(MAX, now)

    return MAX


class TestSolution(unittest.TestCase):
    def test_solution(self):
        self.assertEqual(solution(
            [["15:00", "17:00"], ["16:40", "18:20"], ["14:20", "15:20"], ["14:10", "19:20"], ["18:20", "21:20"]]), 3)

    def test_solution2(self):
        self.assertEqual(solution(
            [["09:10", "10:10"], ["10:20", "12:20"]]), 1)

    def test_solution3(self):
        self.assertEqual(solution(
            [["10:20", "12:30"], ["10:20", "12:30"], ["10:20", "12:30"]]), 3)
