'''
1. 길이가 1인 모든 단어를 포함하도록 사전을 초기화한다.
2. 사전에서 현재 입력과 일치하는 가장 긴 문자열 w를 찾는다.
3. w에 해당하는 사전의 색인 번호를 출력하고, 입력에서 w를 제거한다.
4. 입력에서 처리되지 않은 다음 글자가 남아있다면(c), w+c에 해당하는 단어를 사전에 등록한다.
5. 단계 2로 돌아간다.

주어진 문자열을 압축한 후의 사전 색인 번호를 배열로 출력하라.
'''

msg = 'KAKAO'

def solution(msg):
    answer = []
    lzw_dic = {}

    for i in range(26):
        lzw_dic[chr(65 + i)] = i + 1

    start_idx = 0
    end_idx = start_idx + 1

    while True:
        while msg[start_idx:end_idx] in lzw_dic.keys():
            if end_idx > len(msg):
                break
            end_idx += 1

        w = msg[start_idx:end_idx-1]
        answer.append(lzw_dic[w])
        lzw_dic[msg[start_idx:end_idx]] = len(lzw_dic) + 1

        if end_idx > len(msg):
            break

        start_idx = end_idx - 1
        end_idx = start_idx + 1

    return answer

print(solution(msg))