'''
Demi가 1시간 동안 작업량 1만큼을 처리할 수 있다고 할 때, 
퇴근까지 남은 N 시간과 각 일에 대한 작업량 works에 대해 야근 피로도를 최소화한 값을 리턴하는 함수 solution을 완성해주세요.
'''

works = [4, 3, 3]	
n = 4

import heapq

def solution(n, works):
    heap = []
    
    for work_amount in works:
        heapq.heappush(heap, -work_amount)

    for _ in range(n):
        if heap:
          max_work = -(heapq.heappop(heap))
          if max_work > 1:
            heapq.heappush(heap, -(max_work - 1))
    
    if len(heap) == 0:
       return 0

    return sum([(-num) ** 2 for num in heap])

print(solution(n, works))