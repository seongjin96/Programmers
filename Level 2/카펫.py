'''
Leo가 본 카펫에서 갈색 격자의 수 brown, 노란색 격자의 수 yellow가 매개변수로 주어질 때 카펫의 가로, 세로 크기를 순서대로 배열에 담아 return 하도록 solution 함수를 작성해주세요.
'''

def solution(brown, yellow):
  answer = 0

  x = int(brown / 2 - 1) 
  y = 1

  while (x > 0):
    if y * (x - 2) == yellow:
      break
    
    x -= 1
    y += 1
    
  answer = [x, y + 2]

  return answer