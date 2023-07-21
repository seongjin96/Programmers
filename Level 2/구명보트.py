# 사람들의 몸무게를 담은 배열 people과 구명보트의 무게 제한 limit가 매개변수로 주어질 때,
# 모든 사람을 구출하기 위해 필요한 구명보트 개수의 최솟값을 return 하도록 solution 함수를 작성해주세요.

from collections import deque

people = [70, 50, 80]	
limit = 100

def solution(people, limit):
    answer = 0
    people.sort()
    dq = deque(people)

    while dq:
        if dq[0] + dq[-1] > limit:
            dq.pop()
            answer += 1
            continue
        
        if dq[-1] <= int(limit / 2):
            answer += int((len(dq) + 1) / 2)
            break

        answer += 1
        dq.pop()
        dq.popleft()
    
    return answer


print(solution(people, limit))