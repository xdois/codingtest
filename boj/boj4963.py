import sys
from collections import deque
input = sys.stdin.readline

def bfs(x, y):
    dx = [-1, 1, 0, 0, -1, 1, -1, 1]
    dy = [0, 0, 1, -1, -1, -1, 1, 1]

    queue = deque()
    queue.append((x,y))
    visited[x][y] = True
    
    while queue:
        (x, y) = queue.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < h and 0 <= ny < w and graph[nx][ny] == 1 and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx,ny))
                

if __name__ == '__main__':
    while True:
        w, h = map(int, input().split())
        #print((w,h))
        if w == 0 and h == 0:
            break
        graph = []
        visited = []
        for _ in range(h):
            x = list(map(int, input().split()))
            graph.append(x)
            visited.append([False] * w)
        cnt = 0

        for i in range(h):
            for j in range(w):
                if not visited[i][j] and graph[i][j] == 1:
                    cnt += 1
                    bfs(i,j)

        print(cnt)
        