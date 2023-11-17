'''
문자열 s가 매개변수로 주어질 때, 위 과정과 같이 문자열들로 분해하고, 
분해한 문자열의 개수를 return 하는 함수 solution을 완성하세요.
'''
s = 'banana' # 3 ba - na - na
# s = 'abracadabra' # 6 ab - ra - ca - da - br - a
# s = 'aaabbaccccabba' # 3 aaabbacc - ccab - ba

def solution(s):
    answer = 0

    while True:
        if len(s) <= 1:
            break
        
        x = s[0]
        idx = x_cnt = y_cnt = 0

        while True:
            if s[idx] == x:
                x_cnt += 1
            else:
                y_cnt += 1

            idx += 1

            if x_cnt == y_cnt or idx >= len(s):
              s = s[idx:]
              break
        
        answer += 1

    if len(s) == 1:
        answer += 1

    return answer

print(solution(s))