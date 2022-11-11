import sys
from collections import deque
input = sys.stdin.readline

def bfs(x, y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]

    queue = deque()
    queue.append((x,y))
    #visited[x][y] = True
    
    while queue:
        (x, y) = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1:
                queue.append((nx,ny))
                graph[nx][ny] = graph[x][y] + 1

if __name__ == '__main__':
    n, m = map(int, input().split())
    graph = []
    for i in range(n):
        x = input().rstrip('\n')
        x = list(map(int, x))
        graph.append(x)
        #visited = [False]
    
    bfs(0,0)

    print(graph[n-1][m-1])