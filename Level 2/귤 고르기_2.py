'''
경화가 한 상자에 담으려는 귤의 개수 k와 귤의 크기를 담은 배열 tangerine이 매개변수로 주어집니다. 
경화가 귤 k개를 고를 때 크기가 서로 다른 종류의 수의 최솟값을 return 하도록 solution 함수를 작성해주세요.
'''

from collections import defaultdict
k = 6	
tangerine = [1, 3, 2, 5, 4, 5, 2, 3]

def solution(k, tangerine):
    answer = 0
    
    tangerine_dict = defaultdict(int)

    for num in tangerine:
        tangerine_dict[num] += 1
    
    sorted_tangerine = sorted(tangerine_dict.items(), key = lambda x: x[1], reverse= True)

    for key, value in sorted_tangerine:
        if k <= 0:
          break
        k -= value
        answer += 1
    
    return answer


print(solution(k, tangerine))