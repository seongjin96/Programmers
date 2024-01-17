'''
주차 요금을 나타내는 정수 배열 fees, 자동차의 입/출차 내역을 나타내는 문자열 배열 records가 매개변수로 주어집니다.
차량 번호가 작은 자동차부터 청구할 주차 요금을 차례대로 정수 배열에 담아서 return 하도록 solution 함수를 완성해주세요.
'''

import math
from collections import defaultdict

fees = [180, 5000, 10, 600]
records = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN",
           "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]

def solution(fees, records):
    answer = []
    basic_time, basic_fee, unit_time, unit_fee = fees
    park_history_dic = {}
    park_time_dic = defaultdict(int)

    def get_parking_time(in_time, out_time):
        in_time_list = in_time.split(':')
        out_time_list = out_time.split(':')

        return (int(out_time_list[0]) - int(in_time_list[0])) * 60 + (int(out_time_list[1]) - int(in_time_list[1]))

    def get_parking_fee(parking_time):
        if parking_time <= basic_time:
            return basic_fee
        return basic_fee + int(math.ceil(((parking_time - basic_time) / unit_time))) * unit_fee

    for record in records:
        time, car_id, history = record.split(' ')
        if history == 'IN':
            park_history_dic[car_id] = time
        else:
            parking_time = get_parking_time(park_history_dic[car_id], time)
            park_time_dic[car_id] = park_time_dic[car_id] + parking_time
            park_history_dic[car_id] = ''

    park_history_dic = dict(sorted(park_history_dic.items()))

    for car_id, history in park_history_dic.items():
        if history != '':
            parking_time = get_parking_time(park_history_dic[car_id], '23:59')
            park_time_dic[car_id] = park_time_dic[car_id] + parking_time
        answer.append(get_parking_fee(park_time_dic[car_id]))

    return answer


print(solution(fees, records))
