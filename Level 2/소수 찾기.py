'''
한자리 숫자가 적힌 종이 조각이 흩어져있습니다. 흩어진 종이 조각을 붙여 소수를 몇 개 만들 수 있는지 알아내려 합니다.
각 종이 조각에 적힌 숫자가 적힌 문자열 numbers가 주어졌을 때, 
종이 조각으로 만들 수 있는 소수가 몇 개인지 return 하도록 solution 함수를 완성해주세요.
'''

from itertools import permutations
numbers = "17"

def is_prime(x):
    if x == 0 or x == 1:
        return False
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

def solution(numbers):
    answer = 0
    num_list = []
    all_num_list = set()

    for num in numbers:
        num_list.append(num)

    for i in range(1, len(num_list) + 1):
        for set_list in set(permutations(num_list, i)):
            str_num = ''
            for num in set_list:
                str_num += num
            all_num_list.add(int(str_num))
    
    for num in all_num_list:
        if is_prime(num) == True:
            answer += 1

    return answer

print(solution(numbers))