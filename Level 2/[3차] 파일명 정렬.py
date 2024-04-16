"""
세 차례의 코딩 테스트와 두 차례의 면접이라는 기나긴 블라인드 공채를 무사히 통과해 카카오에 입사한 무지는 파일 저장소 서버 관리를 맡게 되었다.
무지는 단순한 문자 코드 순이 아닌, 파일명에 포함된 숫자를 반영한 정렬 기능을 저장소 관리 프로그램에 구현하기로 했다.
소스 파일 저장소에 저장된 파일명은 100 글자 이내로, 영문 대소문자, 숫자, 공백(" "), 마침표("."), 빼기 부호("-")만으로 이루어져 있다. 파일명은 영문자로 시작하며, 숫자를 하나 이상 포함하고 있다.
무지를 도와 파일명 정렬 프로그램을 구현하라.
"""

import unittest


def separate_files(file):
    idx = 0
    head = ''
    number = ''

    while idx < len(file):
        if file[idx].isdigit():
            break
        head += file[idx]
        idx += 1

    while idx < len(file):
        if not file[idx].isdigit():
            break
        number += file[idx]
        idx += 1

    tail = file[idx:]

    return head, number, tail


def solution(files):
    answer = []
    for idx, file in enumerate(files):
        answer.append(separate_files(file))
    answer.sort(key=lambda x: (x[0].upper(), int(x[1])))
    return [''.join(x) for x in answer]


class TestSolution(unittest.TestCase):
    def test_solution(self):
        self.assertEqual(solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]),
                         ["img1.png", "IMG01.GIF", "img02.png", "img2.JPG", "img10.png", "img12.png"])

    def test_solution2(self):
        self.assertEqual(solution(["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]),
                         ["A-10 Thunderbolt II", "B-50 Superfortress", "F-5 Freedom Fighter", "F-14 Tomcat"])
