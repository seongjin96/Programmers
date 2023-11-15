'''
문자열 배열 babbling이 매개변수로 주어질 때, 
머쓱이의 조카가 발음할 수 있는 단어의 개수를 return하도록 solution 함수를 완성해주세요.
'''

babbling = ["ayaye", "uuu", "yeye", "yemawoo", "ayaayaa"]
enable = ['aya', 'ye', 'woo', 'ma']

def checkExist(babble):
    for sound in enable:
        if babble[:len(sound)] == sound:
            return True
    return False

def solution(babbling):
    answer = 0
    
    for babble in babbling:
        prev = ''
        possible = True
        while True:
            for sound in enable:
                if babble[:len(sound)] == sound:
                    if babble[:len(sound)] == prev:
                        possible = False
                        break
                    else:
                        babble = babble.replace(sound, '', 1)
                        prev = sound
            if possible == False or checkExist(babble) == False:
                break
        if len(babble) == 0:
            answer += 1    
    return answer

print(solution(babbling))