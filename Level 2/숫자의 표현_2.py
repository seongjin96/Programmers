from collections import deque
def solution(n):
    answer = 1
    
    sum = 0
    arr = deque([])
    num = 1
    
    while 1:
        while sum < n:
            sum += num
            arr.append(num)
            num += 1
            if sum == n:
                answer += 1
                break
        sum -= arr.popleft()
        if sum == n:
            answer += 1
        if(arr[-1] > n // 2):
            break
        
    return answer