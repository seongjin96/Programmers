'''
컴퓨터의 개수 n, 연결에 대한 정보가 담긴 2차원 배열 computers가 매개변수로 주어질 때, 
네트워크의 개수를 return 하도록 solution 함수를 작성하시오.
'''

n = 3
computers = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]

from collections import deque

def solution(n, computers):
    answer = 0
    visited = [False] * n
    
    def DFS(i):
        visited[i] = True

        for idx in range(n):
            if computers[i][idx] == 1 and visited[idx] == False:
                DFS(idx)

    def BFS(i):
        queue = deque()
        queue.append(i)

        while queue:
            node = queue.popleft()
            
            for idx in range(n):
                if computers[node][idx] == 1 and visited[idx] == False:
                    visited[idx] = True
                    queue.append(idx)
    
    for i in range(n):
        if visited[i] == False:
            # DFS(i)
            BFS(i)
            answer += 1
    return answer

print(solution(n, computers))