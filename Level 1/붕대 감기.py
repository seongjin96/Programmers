# 붕대 감기 기술의 시전 시간, 1초당 회복량, 추가 회복량을 담은 1차원 정수 배열 bandage와 최대 체력을 의미하는 정수 health,
# 몬스터의 공격 시간과 피해량을 담은 2차원 정수 배열 attacks가 매개변수로 주어집니다.
# 모든 공격이 끝난 직후 남은 체력을 return 하도록 solution 함수를 완성해 주세요.
# 만약 몬스터의 공격을 받고 캐릭터의 체력이 0 이하가 되어 죽는다면 -1을 return 해주세요.


import unittest


def solution(bandage, health, attacks):
    max_health = health
    max_time = attacks[-1][0]
    attack_idx = 0
    continuity = 0

    for time in range(1, max_time + 1):
        if health <= 0:
            break
        if time == attacks[attack_idx][0]:
            health -= attacks[attack_idx][1]
            attack_idx += 1
            continuity = 0
            continue

        health += bandage[1]
        continuity += 1

        if continuity == bandage[0]:
            health += bandage[2]
            continuity = 0

        if health > max_health:
            health = max_health

    if health <= 0:
        return -1

    return health


class TestSolution(unittest.TestCase):
    def test_solution(self):
        self.assertEqual(solution([5, 1, 5], 30, [[2, 10], [9, 15], [10, 5], [11, 5]]), 5)

    def test_solution2(self):
        self.assertEqual(solution([3, 2, 7], 20, [[1, 15], [5, 16], [8, 6]]), -1)

    def test_solution3(self):
        self.assertEqual(solution([4, 2, 7], 20, [[1, 15], [5, 16], [8, 6]]), -1)

    def test_solution4(self):
        self.assertEqual(solution([1, 1, 1], 5, [[1, 2], [3, 2]]), 3)
