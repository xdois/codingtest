# 인접 행렬에서의 bfs -> dx dy 리스트 활용
import sys
input = sys.stdin.readline
from collections import deque

def bfs(x, y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    queue = deque()
    queue.append((x,y))
    visited[x][y] = True
    size = 1

    while queue:
        (x, y) = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == 1 and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx, ny))
                size += 1
    sizes.append(size)

if __name__ == '__main__':
    n = int(input())

    graph = []
    sizes = []

    for _ in range(n):
        x = input().rstrip('\n')
        x = map(int, x)
        graph.append(list(x))
    visited = []
    for _ in range(n):
        visited.append([False] * n)
    cnt = 0
    for i in range(n):
        for j in range(n):
            if not visited[i][j] and graph[i][j] == 1:
                cnt += 1
                bfs(i, j)
                
    print(cnt)
    sizes.sort()
    for s in sizes:
        print(s)
    