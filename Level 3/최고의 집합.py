'''
집합의 원소의 개수 n과 모든 원소들의 합 s가 매개변수로 주어질 때, 
최고의 집합을 return 하는 solution 함수를 완성해주세요.
'''

n = 2
s = 9

def solution(n, s):
    answer = []
    if n > s:
        return [-1]
    
    while n > 0:
        quotient = s // n
        answer.append(quotient)
        s -= quotient
        n -= 1

    return answer

print(solution(n, s))