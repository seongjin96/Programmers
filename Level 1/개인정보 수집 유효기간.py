'''
오늘 날짜를 의미하는 문자열 today, 약관의 유효기간을 담은 1차원 문자열 배열 terms와 수집된 개인정보의 정보를 담은 1차원 문자열 배열 privacies가 매개변수로 주어집니다. 
이때 파기해야 할 개인정보의 번호를 오름차순으로 1차원 정수 배열에 담아 return 하도록 solution 함수를 완성해 주세요.
'''

today = "2022.05.19"
terms =["A 6", "B 12", "C 3"]
privacies = ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]

def solution(today, terms, privacies):
    answer = []
    
    term = {}
    privacy = {}
    
    for t in terms:
        sp = t.split(' ')
        term[sp[0]] = sp[1]
        
    for p in privacies:
        sp = p.split(' ')
        privacy[sp[1]] = list(map(int, sp[0].split('.')))

    print(term)
    print(privacy)
        
    return answer

solution(today, terms, privacies)