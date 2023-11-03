'''
코니가 가진 의상들이 담긴 2차원 배열 clothes가 주어질 때 
서로 다른 옷의 조합의 수를 return 하도록 solution 함수를 작성해주세요.
'''

from collections import defaultdict

# clothes = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]
clothes = [["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]

def solution(clothes):
    answer = 1
    cloth_dict = defaultdict(int)

    for name, type in clothes:
        cloth_dict[type] += 1

    for count in cloth_dict.values():
        answer *= count + 1

    return answer - 1

print(solution(clothes))