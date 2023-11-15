'''
두 정수 left와 right가 매개변수로 주어집니다. 
left부터 right까지의 모든 수들 중에서, 약수의 개수가 짝수인 수는 더하고, 
약수의 개수가 홀수인 수는 뺀 수를 return 하도록 solution 함수를 완성해주세요.
'''

left = 13
right = 17

def get_prime_count(num):
    count = 0
    for i in range (1, int(num ** 0.5) + 1):
        if num % i == 0:
            count += 1
            if int(i ** 2) != num:
                count += 1
    return count

def solution(left, right):
    answer = 0
    for num in range(left, right + 1):
        prime_count = get_prime_count(num)
        if prime_count % 2 == 0:
            answer += num
        else:
            answer -= num
    return answer

print(solution(left, right))