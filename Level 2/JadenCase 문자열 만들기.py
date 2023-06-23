'''
JadenCase란 모든 단어의 첫 문자가 대문자이고, 그 외의 알파벳은 소문자인 문자열입니다.
문자열 s가 주어졌을 때, s를 JadenCase로 바꾼 문자열을 리턴하는 함수, solution을 완성해주세요.
'''

s = "3people  unFollowed me"

def solution(s):
    answer = ''
    word_list = s.lower().split(' ')

    for word in word_list:
        if len(word) == 0:
            answer += ' '
        else:
          answer += word[0].upper() + word[1:len(word)] + ' '

    print(answer)
    return answer[0: len(answer) - 1]

solution(s)