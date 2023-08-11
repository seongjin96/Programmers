'''
상수에게 전해지는 재료의 정보를 나타내는 정수 배열 ingredient가 주어졌을 때, 
상수가 포장하는 햄버거의 개수를 return 하도록 solution 함수를 완성하시오.
'''

ingredient = [2, 1, 1, 2, 3, 1, 2, 3, 1]
# ingredient = [1, 3, 2, 1, 2, 1, 3, 1, 2]

def solution(ingredient):
    answer = 0
    stack = []

    for num in ingredient:
        if num == 1:
          stack.append(num)
        elif stack and num == 2 and stack[-1] == 1:
            stack.append(num)
        elif stack and num == 3 and stack[-1] == 2:
            stack.append(num)
        else:
            stack = []
        
        if len(stack) >= 4:
            if stack[-1] == 1 and stack[-2] == 3:
                answer += 1
                for _ in range(4):
                    stack.pop()

    return answer

print(solution(ingredient))