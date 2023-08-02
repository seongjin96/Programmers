'''
놀이기구를 count번 타게 되면 현재 자신이 가지고 있는 금액에서 얼마가 모자라는지를 return 하도록 solution 함수를 완성하세요.
'''

price = 3
money = 20
count = 4

def solution(price, money, count):
    total = 0

    for num in range(1, count + 1):
        total += num * price

    if total <= money:
        return 0

    return total - money

print(solution(price, money, count))