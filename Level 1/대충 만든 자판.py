'''
1번 키부터 차례대로 할당된 문자들이 순서대로 담긴 문자열배열 keymap과 입력하려는 문자열들이 담긴 문자열 배열 targets가 주어질 때, 
각 문자열을 작성하기 위해 키를 최소 몇 번씩 눌러야 하는지 순서대로 배열에 담아 return 하는 solution 함수를 완성해 주세요.
'''

keymap = ["ABACD", "BCEFD"]	
targets = ["ABCD","AABB"]

def solution(keymap, targets):
    answer = []
    key_dic = {}
    
    for key in keymap:
        for index, k in enumerate(key):
            if k not in key_dic:
                key_dic[k] = index + 1
            else:
                key_dic[k] = min(key_dic[k], index + 1)
    
    for target in targets:
        count = 0
        for k in target:
            if k not in key_dic:
                count = 0
                break
            count += key_dic[k]
        if count != 0:
            answer.append(count)
        else:
            answer.append(-1)
                
    return answer