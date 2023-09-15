'''
사전에 알파벳 모음 'A', 'E', 'I', 'O', 'U'만을 사용하여 만들 수 있는, 길이 5 이하의 모든 단어가 수록되어 있습니다. 
사전에서 첫 번째 단어는 "A"이고, 그다음은 "AA"이며, 마지막 단어는 "UUUUU"입니다.

단어 하나 word가 매개변수로 주어질 때, 이 단어가 사전에서 몇 번째 단어인지 return 하도록 solution 함수를 완성해주세요.
'''

from itertools import product
word = "UUUUU"

def solution(word):
    word_list = ['A', 'E', 'I', 'O', 'U']
    word_dic = []

    for num in range(1, len(word_list) + 1):
        for alpha in product(word_list, repeat = num):
            word_dic.append(''.join(list(alpha)))

    word_dic.sort()
    
    return word_dic.index(word) + 1

print(solution(word))