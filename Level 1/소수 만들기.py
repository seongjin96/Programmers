from itertools import combinations
import math

def isprime(n):
    sqrt = math.sqrt(n)

    if sqrt < 2:
        return False

    for i in range(2, int(sqrt+1)):
        if n % i == 0:
            return False
    return  True

def solution(nums):
    answer = 0
    arr = list(combinations(nums, 3))

    for n1, n2, n3 in arr:
        if isprime(n1+n2+n3):
            answer += 1

    return answer