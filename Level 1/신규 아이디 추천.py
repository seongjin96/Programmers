'''
신규 유저가 입력한 아이디를 나타내는 new_id가 매개변수로 주어질 때, 
네오가 설계한 7단계의 처리 과정을 거친 후의 추천 아이디를 return 하도록 solution 함수를 완성해 주세요.
'''

def solution(new_id):
    answer = ''
    ex = ['_', '-', '.']
    tmp = []
    #1
    answer = new_id.lower()
    
    #2
    str_list = list(answer)
    for str in answer:
        if not str.islower() and str not in ex and not str.isdigit():
            continue
        #3
        if tmp and str == '.':
            if tmp[-1] != '.':
                tmp.append(str)
        #3
        elif not tmp and str == '.':
            continue
        else:
            tmp.append(str)
    #5
    if not tmp:
        tmp.append('a')
    #6
    if len(tmp) >= 16:
        tmp = tmp[:15]
    #4
    if tmp and tmp[-1] == '.':
        tmp.pop()
    #7
    if len(tmp) <= 2:
        while len(tmp) != 3:
            tmp.append(tmp[-1])
    answer = (''.join(tmp))
    
    return answer