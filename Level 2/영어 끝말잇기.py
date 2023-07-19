'''
사람의 수 n과 사람들이 순서대로 말한 단어 words 가 매개변수로 주어질 때, 
가장 먼저 탈락하는 사람의 번호와 그 사람이 자신의 몇 번째 차례에 탈락하는지를 구해서 return 하도록 solution 함수를 완성해주세요.
'''

n = 3
words = ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]

# n = 2
# words = ["hello", "one", "even", "never", "now", "world", "draw"]

def solution(n, words):
    answer = [0, 0]
    word_list = [words[0]]

    for i in range(1, len(words)):
        if words[i - 1][-1] != words[i][0] or words[i] in word_list:
            return [i % n + 1, i // n + 1]
        
        word_list.append(words[i])
            
    return answer

print(solution(n, words))