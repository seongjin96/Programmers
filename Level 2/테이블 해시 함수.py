'''
테이블의 데이터 data와 해시 함수에 대한 입력 col, row_begin, row_end이 주어졌을 때 테이블의 해시 값을 return 하도록 solution 함수를 완성해주세요.
'''


data = [[2,2,6],[1,5,10],[4,2,9],[3,8,3]]
col = 2
row_begin = 2
row_end = 3

def solution(data, col, row_begin, row_end):
    answer = 0
    sorted_data = sorted(data, key=lambda x: (x[col-1], -x[0]))

    for i in range(row_begin - 1, row_end):
        mod_sum = 0
        for num in sorted_data[i]:
            mod_sum += num % (i + 1)
        answer = answer ^ mod_sum

    return answer

print(solution(data, col, row_begin, row_end))