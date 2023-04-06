'''
문자열로 이루어진 배열 cards1, cards2와 원하는 단어 배열 goal이 매개변수로 주어질 때, 
cards1과 cards2에 적힌 단어들로 goal를 만들 있다면 "Yes"를, 만들 수 없다면 "No"를 return하는 solution 함수를 완성해주세요.
'''

def solution(cards1, cards2, goal):
    answer = ''
    cards1.reverse()
    cards2.reverse()
    goal.reverse()

    while (goal):
        if cards1 and goal[-1] == cards1[-1]:
            goal.pop()
            cards1.pop()
            continue
        if cards2 and goal[-1] == cards2[-1]:
            goal.pop()
            cards2.pop()
            continue
        return "No"
        
    return "Yes"