'''
회원등록시 정현이가 원하는 제품을 모두 할인 받을 수 있는 회원등록 날짜의 총 일수를 return 하는 solution 함수를 완성하시오.
'''

want = ["banana", "apple", "rice", "pork", "pot"]
number = [3, 2, 2, 2, 1]
discount = ["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"]

# want = ["apple"]
# number = [10]
# discount = ["banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana"]

def solution(want, number, discount):
    answer = 0
    want_list = []

    for item, count in zip(want, number):
        for _ in range(count):
            want_list.append(item)
            
    want_list.sort()

    for i in range(len(discount)):
        items = discount[i : i + 10]
        items.sort()

        if want_list == items:
            answer += 1

    return answer

print(solution(want, number, discount))