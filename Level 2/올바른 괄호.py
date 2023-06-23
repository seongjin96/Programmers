'''
'(' 또는 ')' 로만 이루어진 문자열 s가 주어졌을 때, 문자열 s가 올바른 괄호이면 true를 return 하고,
올바르지 않은 괄호이면 false를 return 하는 solution 함수를 완성해 주세요.
'''

s = "(())()"
def solution(s):
    stack = []

    for str in s:
        if str == '(':
            stack.append(str)
            continue
        if not stack and str == ')':
            return False
        stack.pop()

    if stack:
        return False    

    return True

solution(s)