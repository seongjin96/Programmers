'''
피보나치 수는 F(0) = 0, F(1) = 1일 때, 1 이상의 n에 대하여 F(n) = F(n-1) + F(n-2) 가 적용되는 수 입니다.
2 이상의 n이 입력되었을 때, n번째 피보나치 수를 1234567으로 나눈 나머지를 리턴하는 함수, solution을 완성해 주세요.
'''

n = 100000

def solution(n):
  if n == 0 or n == 1:
    return n
  
  dp = [0 for _ in range(n + 1)]
  dp[1] = 1

  for i in range(2, n + 1):
    dp[i] = (dp[i - 1] + dp[i - 2]) % 1234567

  return dp[n]

print(solution(n))