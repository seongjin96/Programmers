'''
두 정수 X, Y가 주어졌을 때, X, Y의 짝꿍을 return하는 solution 함수를 완성해주세요.
'''

X = "100"	
Y = "203045"

from collections import defaultdict

def solution(X, Y):
    answer = ''

    x_dict = defaultdict(int)
    same_list = list()
    
    for num in X:
        x_dict[num] += 1

    for num in Y:
        if x_dict[num] != 0:
            same_list.append(num)
            x_dict[num] -= 1
    
    same_list.sort(reverse= True)

    if not same_list:
        return '-1'
    if same_list[0] == '0':
        return '0'
    
    for num in same_list:
        answer += num
    return answer


print(solution(X, Y))