'''
멀리뛰기에 사용될 칸의 수 n이 주어질 때, 효진이가 끝에 도달하는 방법이 몇 가지인지 알아내, 
여기에 1234567를 나눈 나머지를 리턴하는 함수, solution을 완성하세요.
'''

n = 4

def solution(n):
    arr = [0 for _ in range(2001)]
    arr[1] = 1
    arr[2] = 2

    for i in range(3, n + 1):
        arr[i] = (arr[i - 2] + arr[i - 1]) % 1234567

    return arr[n]


print(solution(n))