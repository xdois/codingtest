# 인접행렬 bfs
# 인접한 4방향에 graph값이 0이면 1로 -1이면 스킵
# 서로 다른 토마토에서 동시에 출발하는것은 어떻게 할 것인가
# -> 큐에 1인 좌표들을 전부 넣는다
# 굳이 visited 배열이 필요가 없다

import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]
    while queue:
        (x, y) = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
                graph[nx][ny] += graph[x][y] + 1
                queue.append((nx,ny))

if __name__ == '__main__':
    m, n = map(int, input().split())
    graph = []

    for _ in range(n):
        x = list(map(int, input().split()))
        graph.append(x)

    queue = deque()
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                queue.append((i,j))

    bfs()
    isZero = False
    ans = -2
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                isZero = True
            ans = max(ans, graph[i][j])
    if isZero:
        print(-1)
    else:
        print(ans - 1)
    
