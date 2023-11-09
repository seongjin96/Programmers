'''
특정 튜플을 표현하는 집합이 담긴 문자열 s가 매개변수로 주어질 때, 
s가 표현하는 튜플을 배열에 담아 return 하도록 solution 함수를 완성해주세요.
'''

from collections import defaultdict

# s = "{{2},{2,1},{2,1,3},{2,1,3,4}}"
s = "{{20,111},{111}}"

def solution(s):
    answer = []
    idx = 0
    count_dict = defaultdict(int)

    while idx < len(s):
        str_num = ''

        if s[idx].isalnum():
            while s[idx].isalnum():
                str_num += s[idx]
                idx+= 1

            count_dict[int(str_num)] += 1

        idx += 1
    
    ordered_count_dict = sorted(count_dict.items(), key=lambda x: x[1], reverse=True)

    for key, value in ordered_count_dict:
        answer.append(key)
        
    return answer

print(solution(s))