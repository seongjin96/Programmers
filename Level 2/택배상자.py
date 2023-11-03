'''
택배 기사님이 원하는 상자 순서를 나타내는 정수 배열 order가 주어졌을 때, 
영재가 몇 개의 상자를 실을 수 있는지 return 하는 solution 함수를 완성하세요.
'''

order = [5, 4, 3, 2, 1]

def solution(order):
    answer = 0
    spare = [0,]
    order.reverse()
    box_num = 1

    while order:
        if order[-1] != box_num and order[-1] != spare[-1] and order[-1] < box_num:
            break
        if order[-1] == spare[-1]:
            order.pop()
            spare.pop()
            answer += 1
        else:
            spare.append(box_num)
            box_num += 1
    
    return answer

print(solution(order))