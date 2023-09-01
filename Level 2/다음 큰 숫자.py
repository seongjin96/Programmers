'''
자연수 n이 매개변수로 주어질 때, n의 다음 큰 숫자를 return 하는 solution 함수를 완성해주세요.
'''

n = 78

def solution(n):
    i = 0
    cnt = 0
    big_cnt = 0
    init_num = n
    
    while(n):
        if n % 2 == 1:
            cnt += 1
        n = n // 2

    while(1):
        i += 1
        big_num = init_num + i
        big_cnt = 0

        while(big_num):
            if big_num % 2 == 1:
                big_cnt += 1
            cal_num = cal_num // 2

        if cnt == big_cnt:
            return init_num + i
        
    return 0
    
    


print(solution(n))