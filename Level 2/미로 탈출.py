'''
미로를 나타낸 문자열 배열 maps가 매개변수로 주어질 때,
미로를 탈출하는데 필요한 최소 시간을 return 하는 solution 함수를 완성해주세요.
만약, 탈출할 수 없다면 -1을 return 해주세요.
'''

maps = ["SOOOL","XXXXO","OOOOO","OXXXX","OOOOE"]
# maps = ["LOOXS","OOOOX","OOOOO","OOOOO","EOOOO"]

from collections import deque

def solution(maps):
    answer = 0

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    n = len(maps[0])
    m = len(maps)
    visited = [[0] * n for _ in range(m)]

    def bfs(x, y, cnt):
        nonlocal visited
        is_open = False
        queue = deque()
        queue.append((x, y, cnt))

        while queue:
            x, y, cnt = queue.popleft()

            if is_open and maps[y][x] == 'E':
                return cnt

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if nx < 0 or nx >= n or ny < 0 or ny >= m:
                    continue
                if maps[ny][nx] == 'X' or visited[ny][nx] == 1:
                    continue
                if maps[ny][nx] == 'L':
                    is_open = True
                    visited = [[0] * n for _ in range(m)]
                    queue.clear()
                    queue.append((nx, ny, cnt + 1))
                    visited[ny][nx] = 1
                    break
                queue.append((nx, ny, cnt + 1))
                visited[ny][nx] = 1

        return -1

    for y in range(m):
        for x in range(n):
            if maps[y][x] == 'S':
                answer = bfs(x, y, 0)
                break

    return answer

print(solution(maps))