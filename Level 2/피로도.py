'''
이 게임에는 하루에 한 번씩 탐험할 수 있는 던전이 여러개 있는데, 한 유저가 오늘 이 던전들을 최대한 많이 탐험하려 합니다. 
유저의 현재 피로도 k와 각 던전별 "최소 필요 피로도", "소모 피로도"가 담긴 2차원 배열 dungeons 가 매개변수로 주어질 때, 
유저가 탐험할수 있는 최대 던전 수를 return 하도록 solution 함수를 완성해주세요.
'''

from itertools import permutations

k = 80
dungeons = [[80,20],[50,40],[30,10]]


def solution(k, dungeons):
    max_count = 0
    init = []

    for i in range(len(dungeons)):
        init.append(i)
    
    for permutaion in permutations(init, len(dungeons)):
        use = k
        count = 0

        for num in permutaion:
            if use >= dungeons[num][0]:
                use -= dungeons[num][1]
                count += 1
        max_count = max(count, max_count)

    return max_count


print(solution(k, dungeons))