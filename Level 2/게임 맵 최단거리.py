'''
게임 맵의 상태 maps가 매개변수로 주어질 때, 캐릭터가 상대 팀 진영에 도착하기 위해서 지나가야 하는 칸의 개수의 최솟값을 return 하도록 solution 함수를 완성해주세요. 
단, 상대 팀 진영에 도착할 수 없을 때는 -1을 return 해주세요.
'''

from collections import deque

# maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]
maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]

def solution(maps):
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    
    n = len(maps[0])
    m = len(maps)

    visited = [[0] * n for _ in range(m)]

    def bfs(x, y, cnt):
        queue = deque()
        queue.append((x, y, cnt))

        while queue:
            x, y, cnt = queue.popleft()

            if x == n - 1 and y == m - 1:
                return cnt + 1

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if nx < 0 or nx >= n or ny < 0 or ny >= m:
                    continue
                if (visited[ny][nx] == 1):
                    continue
                if (maps[ny][nx] == 1):
                    queue.append((nx, ny, cnt + 1))
                    visited[ny][nx] = 1
        return -1
    
    return bfs(0, 0, 0)
    
print(solution(maps))