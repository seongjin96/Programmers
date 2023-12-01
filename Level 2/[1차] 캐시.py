'''
어피치에게 시달리는 제이지를 도와, DB 캐시를 적용할 때 캐시 크기에 따른 실행시간 측정 프로그램을 작성하시오.
'''

cacheSize = 3
cities = ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]

from collections import deque

def solution(cacheSize, cities):
    time = 0
    cache = deque()
    
    for city in cities:
        if city.upper() in cache:
            cache.remove(city.upper())
            cache.append(city.upper())
            time += 1
            continue
        
        cache.append(city.upper())

        if len(cache) > cacheSize:
            cache.popleft()

        time += 5
            
    return time

print(solution(cacheSize, cities))