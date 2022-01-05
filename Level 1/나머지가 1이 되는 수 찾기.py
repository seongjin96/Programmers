import math

def solution(n):
    x = n - 1
    if x % 2 == 0:
        return 2
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return i
    return x