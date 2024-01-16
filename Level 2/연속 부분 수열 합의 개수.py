'''
원형 수열의 모든 원소 elements가 순서대로 주어질 때,
원형 수열의 연속 부분 수열 합으로 만들 수 있는 수의 개수를 return 하도록 solution 함수를 완성해주세요.
'''

elements = [7, 9, 1, 1, 4]

def solution(elements):
    answer = set()
    count = len(elements)
    multiple_elements = elements * 2

    for i in range(1, count + 1):
        for j in range(count):
            answer.add(sum(multiple_elements[j:i+j]))

    return len(answer)

print(solution(elements))
