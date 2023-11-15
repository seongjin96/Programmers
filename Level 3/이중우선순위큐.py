'''
이중 우선순위 큐가 할 연산 operations가 매개변수로 주어질 때, 
모든 연산을 처리한 후 큐가 비어있으면 [0,0] 비어있지 않으면 [최댓값, 최솟값]을 return 하도록 solution 함수를 구현해주세요.
'''

# operations = ["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]
operations = ["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]

import heapq

def solution(operations):
    max_hip = []
    min_hip = []

    for operation in operations:
        command, num = operation.split(' ')
        num = int(num)
        if command == 'I':
            heapq.heappush(max_hip, -num)
            heapq.heappush(min_hip, num)
            continue
        if command == 'D' and max_hip:
            if num == 1:
              min_hip.remove(-(heapq.heappop(max_hip)))
            else:
              max_hip.remove(-(heapq.heappop(min_hip)))

    if len(max_hip) == 0:
        return [0, 0]
    
    return [-(heapq.heappop(max_hip)), heapq.heappop(min_hip)]

print(solution(operations))