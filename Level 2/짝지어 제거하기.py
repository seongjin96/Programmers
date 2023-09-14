'''
문자열 S가 주어졌을 때, 짝지어 제거하기를 성공적으로 수행할 수 있는지 반환하는 함수를 완성해 주세요. 
성공적으로 수행할 수 있으면 1을, 아닐 경우 0을 리턴해주면 됩니다.
'''

s = 'baabaa'

def solution(s):
    stack = []
    for ch in s:
        if not stack:
            stack.append(ch)
        else:
            if stack[-1] == ch:
                stack.pop()
            else:
                stack.append(ch)
    
    if not stack:
        return 1
    else:
        return 0

print(solution(s))