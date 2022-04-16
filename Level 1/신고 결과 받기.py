'''
이용자의 ID가 담긴 문자열 배열 id_list, 각 이용자가 신고한 이용자의 ID 정보가 담긴 문자열 배열 report, 정지 기준이 되는 신고 횟수 k가 매개변수로 주어질 때,
각 유저별로 처리 결과 메일을 받은 횟수를 배열에 담아 return 하도록 solution 함수를 완성해주세요.
'''

def solution(id_list, report, k):
    answer = []
    id_dict = {}
    count_dict = {}
    stop_member = []
    
    for id in id_list:
        id_dict[id] = []
        count_dict[id] = 0
    
    for i in range(len(report)):
        id, reported_id  = report[i].split(' ')
        if reported_id not in id_dict[id]:
            id_dict[id].append(reported_id)
            count_dict[reported_id] += 1
            if reported_id not in stop_member and count_dict[reported_id] >= k:
                stop_member.append(reported_id)
    
    for i in range(len(id_list)):
        cnt = 0
        for member in stop_member:
            if member in id_dict[id_list[i]]:
                cnt += 1
        answer.append(cnt)
    
    return answer