'''
아이언 슈트 구매자가 이동하려는 거리 N이 주어졌을 때, 사용해야 하는 건전지 사용량의 최솟값을 return하는 solution 함수를 만들어 주세요.
'''

n = 6

def solution(n):
    ans = 0

    while n > 0:
        if n % 2 == 1:
            ans += 1
        n = n // 2
    
    return ans

print(solution(n))