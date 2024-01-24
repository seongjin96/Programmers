'''
data에서 ext 값이 val_ext보다 작은 데이터만 뽑은 후, sort_by에 해당하는 값을 기준으로 오름차순으로 정렬하여 return 하도록 solution 함수를 완성해 주세요.
단, 조건을 만족하는 데이터는 항상 한 개 이상 존재합니다.
'''

data = [[1, 20300104, 100, 80], [2, 20300804, 847, 37], [3, 20300401, 10, 8]]
ext = 'date'
val_ext = 20300501
sort_by = 'remain'

def solution(data, ext, val_ext, sort_by):
    answer = []
    idx_map = {
        'code': 0,
        'date': 1,
        'maximum': 2,
        'remain': 3
    }

    for item in data:
        if item[idx_map[ext]] < val_ext:
            answer.append(item)

    answer.sort(key=lambda x: x[idx_map[sort_by]])

    return answer

print(solution(data, ext, val_ext, sort_by))