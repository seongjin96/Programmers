'''
채팅방에 들어오고 나가거나, 닉네임을 변경한 기록이 담긴 문자열 배열 record가 매개변수로 주어질 때, 
모든 기록이 처리된 후, 최종적으로 방을 개설한 사람이 보게 되는 메시지를 문자열 배열 형태로 return 하도록 solution 함수를 완성하라.
'''

record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]

def solution(record):
    answer = []
    user_dict = {}
    
    for history in record:
        history_arr = history.split(' ')

        if history_arr[0] == 'Leave':
            continue

        user_dict[history_arr[1]] = history_arr[2]

    for history in record:
        history_arr = history.split(' ')
        nick = user_dict[history_arr[1]]
        
        if history_arr[0] == 'Enter':
            answer.append(nick + '님이 들어왔습니다.')
        if history_arr[0] == 'Leave':
            answer.append(nick + '님이 나갔습니다.')
    
    return answer

print(solution(record))