'''
문자열 s가 주어졌을 때, s의 각 위치마다 자신보다 앞에 나왔으면서, 자신과 가장 가까운 곳에 있는 같은 글자가 어디 있는지 알고 싶습니다.
문자열 s이 주어질 때, 위와 같이 정의된 연산을 수행하는 함수 solution을 완성해주세요.
'''

def solution(s):
    answer = []
    dic = dict()
    
    for i in range(len(s)):
        if s[i] not in dic:
            answer.append(-1)
        else:
            answer.append(i - dic[s[i]])
        dic[s[i]] = i
    return answer