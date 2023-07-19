'''
마지막 행까지 모두 내려왔을 때, 얻을 수 있는 점수의 최대값을 return하는 solution 함수를 완성해 주세요.
'''

land = [[1,2,3,5],[5,6,7,8],[4,3,2,1]]

def solution(land):
    N = 4
    
    # land 배열 크기만큼 0으로 초기화
    dp = [[0] * N for _ in range(len(land))]
    dp[0] = land[0]

    # dp배열에 각 최대값을 세팅
    for i in range(1, len(land)):
        for j in range(N):
            max_num = 0
            for k in range(N):
                if j == k:
                    continue
                max_num = max(max_num, dp[i - 1][k])    
            dp[i][j] = land[i][j] + max_num   

    return max(dp[len(land) - 1])


print(solution(land))