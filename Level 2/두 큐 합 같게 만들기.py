'''
길이가 같은 두 개의 큐를 나타내는 정수 배열 queue1, queue2가 매개변수로 주어집니다. 각 큐의 원소 합을 같게 만들기 위해 필요한 작업의 최소 횟수를 return 하도록 solution 함수를 완성해주세요. 
단, 어떤 방법으로도 각 큐의 원소 합을 같게 만들 수 없는 경우, -1을 return 해주세요.
'''

# queue1 = [3, 2, 7, 2]
# queue2 = [4, 6, 5, 1]

# queue1 = [1, 2, 1, 2]
# queue2 = [1, 10, 1, 2]

queue1 = [1, 29]
queue2 = [30, 2]

from collections import deque

def solution(queue1, queue2):
    answer = 0
    
    queue1 = deque(queue1)
    queue2 = deque(queue2)

    sum_1 = sum(queue1)
    sum_2 = sum(queue2)
    
    max_cnt = (len(queue1) + len(queue2) * 2)

    if (sum_1 + sum_2) % 2 != 0:
        return -1

    while sum_1 != sum_2:
        if sum_1 == 0 or sum_2 == 0 or answer >= max_cnt:
            return -1
        
        if sum_1 > sum_2:
            pop_num = queue1.popleft()
            queue2.append(pop_num)
            sum_1 -= pop_num
            sum_2 += pop_num
        elif sum_1 < sum_2:
            pop_num = queue2.popleft()
            queue1.append(pop_num)
            sum_1 += pop_num
            sum_2 -= pop_num
        answer += 1
          
    return answer

print(solution(queue1, queue2))