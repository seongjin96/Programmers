'''
경화가 한 상자에 담으려는 귤의 개수 k와 귤의 크기를 담은 배열 tangerine이 매개변수로 주어집니다. 
경화가 귤 k개를 고를 때 크기가 서로 다른 종류의 수의 최솟값을 return 하도록 solution 함수를 작성해주세요.
'''

def solution(k, tangerine):
    answer = 0
        
    tlist = [0 for _ in range(10000001)]
    
    for num in tangerine:
        tlist[num] += 1
        
    tlist.sort(reverse = True)
    
    for num in tlist:
        answer += 1
        k = k - num
        if k <= 0:
            break
    return answer