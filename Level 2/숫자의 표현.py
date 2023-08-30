'''
자연수 n이 매개변수로 주어질 때, 연속된 자연수들로 n을 표현하는 방법의 수를 return하는 solution를 완성해주세요.
'''

n = 16

from collections import deque
def solution(n):
    answer = 1

    sum = 0
    sum_list = deque([])
    half = n // 2 + 1
    
    while half > 0:
        while sum < n:
           sum += half
           sum_list.append(half)
           half -= 1
           print(sum_list)
           if sum == n:
               answer += 1
               break
        sum -= sum_list.popleft()

    return answer

print(solution(n))