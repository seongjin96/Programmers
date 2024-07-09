# 자연수 x를 y로 변환하려고 합니다. 사용할 수 있는 연산은 다음과 같습니다.
#
# x에 n을 더합니다
# x에 2를 곱합니다.
# x에 3을 곱합니다.

# 자연수 x, y, n이 매개변수로 주어질 때, x를 y로 변환하기 위해 필요한 최소 연산 횟수를 return하도록 solution 함수를 완성해주세요.
# 이때 x를 y로 만들 수 없다면 -1을 return 해주세요.

import unittest
from collections import deque


def solution(x, y, n):
    visited = [False for _ in range(y + 1)]

    def bfs(num, cnt):
        visited[num] = True
        queue = deque()
        queue.append((num, cnt))

        while queue:
            num, cnt = queue.popleft()

            if num == y:
                return cnt

            for i in range(3):
                c_num = num

                if i == 0:
                    c_num += n
                elif i == 1:
                    c_num = num * 2
                else:
                    c_num = num * 3

                if c_num > y or visited[c_num]:
                    continue
                else:
                    queue.append((c_num, cnt + 1))
                    visited[c_num] = True

        return -1

    return bfs(x, 0)


class Test(unittest.TestCase):
    def test_solution(self):
        self.assertEqual(solution(10, 40, 5), 2)

    def test_solution2(self):
        self.assertEqual(solution(10, 40, 30), 1)

    def test_solution3(self):
        self.assertEqual(solution(2, 5, 4), -1)
