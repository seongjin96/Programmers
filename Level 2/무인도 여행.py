'''
지도를 나타내는 문자열 배열 maps가 매개변수로 주어질 때,
각 섬에서 최대 며칠씩 머무를 수 있는지 배열에 오름차순으로 담아 return 하는 solution 함수를 완성해주세요.
만약 지낼 수 있는 무인도가 없다면 -1을 배열에 담아 return 해주세요.
'''

maps = ["X591X","X1X5X","X231X", "1XXX1"]

from collections import deque

def solution(maps):
    answer = []

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    n = len(maps[0])
    m = len(maps)

    visited = [[0] * n for _ in range(m)]

    def bfs(x, y):
        queue = deque()
        queue.append((x, y))
        days = int(maps[y][x])

        while queue:
            x, y = queue.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < n and 0 <= ny < m and visited[ny][nx] == 0 and maps[ny][nx] != 'X':
                    visited[ny][nx] = 1
                    queue.append((nx, ny))
                    days += int(maps[ny][nx])

        return days

    for y in range(m):
        for x in range(n):
            if visited[y][x] == 0 and maps[y][x] != 'X':
                visited[y][x] = 1
                answer.append(bfs(x, y))

    if len(answer) == 0:
        return [-1]

    answer.sort()

    return answer

print(solution(maps))