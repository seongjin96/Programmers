'''
정수 n, m과 다시 페인트를 칠하기로 정한 구역들의 번호가 담긴 정수 배열 section이 매개변수로 주어질 때 
롤러로 페인트칠해야 하는 최소 횟수를 return 하는 solution 함수를 작성해 주세요.
'''

def solution(n, m, section):
    answer = 0
    
    # 구역을 다 칠할때까지 반복문
    while (section):
        # 마지막 구역부터 페인트 그리기 시작
        start = section[-1]
        # 롤러의 길이가 마지막 섹션보다 클 경우
        # 마지막 구역을 롤러의 길이로 설정
        if start < m:
            start = m
        # 페인트를 칠하기 시작한 구역부터 롤러의 길이만큼 칠했을 때
        # 구역이 포함되어 있으면 해당 구역 제외
        while (section and start - m + 1 <= section[-1]):
            section.pop()
        answer += 1
            
    return answer