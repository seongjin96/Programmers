'''
문자열 input_string이 주어졌을 때, 외톨이 알파벳들을 알파벳순으로 이어 붙인 문자열을 return 하도록 solution 함수를 완성해주세요. 
만약, 외톨이 알파벳이 없다면 문자열 "N"을 return 합니다.
'''

input_string = "edeaaabbccd"

def solution(input_string):
    answer = ''
    stack = []
    answer_list = []

    for str in input_string:
        if not stack or stack[-1] != str:
            stack.append(str)
    print(stack)
    for str in set(stack):
        if stack.count(str) >= 2:
            answer_list.append(str)
    
    if len(answer_list) == 0:
        return 'N'
    print(answer_list)
    answer_list.sort()

    for str in answer_list:
        answer += str
    return answer

print(solution(input_string))