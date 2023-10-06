'''
게임 참가자 수 N, 참가자 번호 A, 경쟁자 번호 B가 함수 solution의 매개변수로 주어질 때, 
처음 라운드에서 A번을 가진 참가자는 경쟁자로 생각하는 B번 참가자와 몇 번째 라운드에서 만나는지 return 하는 solution 함수를 완성해 주세요. 
단, A번 참가자와 B번 참가자는 서로 붙게 되기 전까지 항상 이긴다고 가정합니다.
'''

n = 8
a = 4
b = 7

def solution(n,a,b):
    answer = 0
    
    while True:
        a = (a // 2) + (a % 2)
        b = (b // 2) + (b % 2)
        answer += 1

        if a == b:
            return answer

print(solution(n, a, b))