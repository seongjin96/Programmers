'''
수웅이가 준비한 음식의 양을 칼로리가 적은 순서대로 나타내는 정수 배열 food가 주어졌을 때, 
대회를 위한 음식의 배치를 나타내는 문자열을 return 하는 solution 함수를 완성해주세요.
'''

def solution(food):
    answer = ''
    
    for i in range(1, len(food)):
        answer += str(i) * (food[i] // 2)
    reversed_answer = answer[::-1]
    answer += '0'
    answer += reversed_answer
    return answer