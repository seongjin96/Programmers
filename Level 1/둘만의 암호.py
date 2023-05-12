'''
두 문자열 s와 skip, 그리고 자연수 index가 매개변수로 주어질 때 위 규칙대로 s를 변환한 결과를 return하도록 solution 함수를 완성해주세요.
'''

def solution(s, skip, index):
    answer = ''
    skiplist = []
    init = ord('a')
    end = ord('z') + 1

    for str in skip:
        skiplist.append(ord(str))

    for str in s:
        idx = 1
        ord_num = ord(str)
        while (idx < index + 1):
            ord_num += 1
            if ord_num == end:
                ord_num = init
            if ord_num not in skiplist:
                idx += 1
        answer += chr(ord_num)
        
    return answer