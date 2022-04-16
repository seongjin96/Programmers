'''
모든 명함의 가로 길이와 세로 길이를 나타내는 2차원 배열 sizes가 매개변수로 주어집니다. 
모든 명함을 수납할 수 있는 가장 작은 지갑을 만들 때, 지갑의 크기를 return 하도록 solution 함수를 완성해주세요.
'''

def solution(sizes):
    answer = 0
    width_max = 0
    height_max = 0
    
    for i in range(len(sizes)):
        sizes[i].sort()
        width_max = max(width_max, sizes[i][0])
        height_max = max(height_max, sizes[i][1])
        
    answer = width_max * height_max
        
    return answer