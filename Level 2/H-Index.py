'''
어떤 과학자가 발표한 논문의 인용 횟수를 담은 배열 citations가 매개변수로 주어질 때, 
이 과학자의 H-Index를 return 하도록 solution 함수를 작성해주세요.
'''

citations = [3, 0, 6, 1, 5]

def solution(citations):
    answer = 0
    citations.sort(reverse = True)

    for index in range(len(citations)):
        if citations[index] <= answer:
            break
        answer += 1

    return answer

print(solution(citations))