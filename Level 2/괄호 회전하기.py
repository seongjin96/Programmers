'''
대괄호, 중괄호, 그리고 소괄호로 이루어진 문자열 s가 매개변수로 주어집니다. 
이 s를 왼쪽으로 x (0 ≤ x < (s의 길이)) 칸만큼 회전시켰을 때 
s가 올바른 괄호 문자열이 되게 하는 x의 개수를 return 하도록 solution 함수를 완성해주세요.
'''

from collections import deque

def checkStr(str):
    q = []
    start = ['{', '(', '[']
    end = ['}', ')', ']']
    
    for i in str:
        if i in start:
            q.append(i)
        else:
            idx = end.index(i)
            if not q or q[-1] != start[idx]:
                return False
            else:
                q.pop()
    if len(q) == 0:
        return True
    else:
        return False

def solution(s):
    answer = 0
    s = deque(s)
        
    for _ in range(len(s)):
        s.append(s.popleft())

        if checkStr(s):
            answer += 1
        
    return answer