'''
명령어가 매개변수 dirs로 주어질 때, 게임 캐릭터가 처음 걸어본 길의 길이를 구하여 return 하는 solution 함수를 완성해 주세요.
'''

dirs = "ULURRDLLU"

def solution(dirs):
    max_path_length = 11
    dx = max_path_length // 2
    dy = max_path_length // 2

    path_list = set()

    for dir in dirs:
        x = dx
        y = dy

        if dir == 'U' and dy - 1 >= 0:
            dy -= 1
        elif dir == 'D' and dy + 1 < max_path_length:
            dy += 1
        elif dir == 'L' and dx - 1 >= 0:
            dx -= 1
        elif dir == 'R' and dx + 1 < max_path_length:
            dx += 1
        else:
            continue

        if (y, x, dy, dx) not in path_list and (dy, dx, y, x) not in path_list:
            path_list.add((y, x, dy, dx))

    return len(path_list)

print(solution(dirs))