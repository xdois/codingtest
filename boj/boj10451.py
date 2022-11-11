from collections import deque
import sys
input = sys.stdin.readline

def bfs(edges, v, visited):
    queue = deque([v])
    visited[v] = True

    while queue:
        now = queue.popleft()
        
        for e in edges[now]:
            if not visited[e]:
                queue.append(e)
                visited[e] = True

if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        N = int(input())
        arr = list(map(int, input().split()))
        edges = [[] for _ in range(N+1)]
        for i in range(N):
            edges[i+1].append(arr[i])

        visited = [False] * (N+1)
        cnt = 0
        for i in range(1, N+1):
            if not visited[i]:
                bfs(edges, i, visited)
                cnt += 1
                #print(i)
        print(cnt)
