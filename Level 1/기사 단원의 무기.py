'''
기사단원의 수를 나타내는 정수 number와 이웃나라와 협약으로 정해진 공격력의 제한수치를 나타내는 정수 limit와 
제한수치를 초과한 기사가 사용할 무기의 공격력을 나타내는 정수 power가 주어졌을 때, 
무기점의 주인이 무기를 모두 만들기 위해 필요한 철의 무게를 return 하는 solution 함수를 완성하시오.
'''

number = 5
limit = 3
power	= 2

def get_prime_count(n):
    count = 0
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            count += 1
            if i**2 != n:
                count += 1
    return count

def solution(number, limit, power):
    answer = 0
    prime_list = []
    for i in range(1, number + 1):
        prime_list.append(get_prime_count(i))
    
    for num in prime_list:
        if num > limit:
            answer += power
        else:
            answer += num
    return answer