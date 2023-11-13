'''
공원을 나타내는 문자열 배열 park, 로봇 강아지가 수행할 명령이 담긴 문자열 배열 routes가 매개변수로 주어질 때, 
로봇 강아지가 모든 명령을 수행 후 놓인 위치를 [세로 방향 좌표, 가로 방향 좌표] 순으로 배열에 담아 return 하도록 solution 함수를 완성해주세요.
'''

park = ["SOO", "OOO", "OOO"]
routes = ["E 2", "S 2", "W 1"]

def solution(park, routes):
    park_list = [[1] * len(park[0]) for _ in range(len(park))]
    x = y = 0
    
    for i in range(len(park)):
        for j in range(len(park[i])):
            if park[i][j] == 'S':
                x = i
                y = j
            if park[i][j] == 'X':
                park_list[i][j] = 0

    for path in routes:
        direction, move = path.split(' ')
        move = int(move)
        start_x = x
        start_y = y

        if direction == 'E':
            for i in range(start_y, start_y+move):
                y += 1
                if y >= len(park[0]) or not park_list[x][y] or park_list[x][y] == 0:
                    y = start_y
                    break
        elif direction == 'W':
            for i in range(start_y, start_y-move, -1):
                y -= 1
                if y < 0 or not park_list[x][y] or park_list[x][y] == 0:
                    y = start_y
                    break
        elif direction == 'S':
            for i in range(start_x, start_x+move):
                x += 1
                if x >= len(park) or not park_list[x][y] or park_list[x][y] == 0:
                    x = start_x
                    break
        elif direction == 'N':
            for i in range(start_x, start_x-move, -1):
                x -= 1
                if x < 0 or not park_list[x][y] or park_list[x][y] == 0:
                    x = start_x
                    break
    return [x, y]

print(solution(park, routes))