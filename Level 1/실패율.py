'''
전체 스테이지의 개수 N, 게임을 이용하는 사용자가 현재 멈춰있는 스테이지의 번호가 담긴 배열 stages가 매개변수로 주어질 때, 
실패율이 높은 스테이지부터 내림차순으로 스테이지의 번호가 담겨있는 배열을 return 하도록 solution 함수를 완성하라.
'''

N = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]

# result = [3, 4, 2, 1, 5]

def solution(N, stages):
    answer = []
    total_fail_cnt = 0
    fail_rate_dict = {}
    
    for i in range(1, N + 1):
        stage_fail_cnt = 0
        left_cnt = len(stages) - total_fail_cnt

        if left_cnt == 0:
            fail_rate_dict[i] = 0
            continue
        for stage in stages:
            if i == stage:
                total_fail_cnt += 1
                stage_fail_cnt += 1
        
        fail_rate_dict[i] = stage_fail_cnt / left_cnt

    sorted_dict = sorted(fail_rate_dict.items(), key=lambda x: x[1], reverse=True)

    for stage, fail_rate in sorted_dict:
        answer.append(stage)

    return answer


print(solution(N, stages))