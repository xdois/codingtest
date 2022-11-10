from collections import deque
import sys

input = sys.stdin.readline

N, M = map(int, input().split())

edges = [[] for _ in range(N + 1)]

for _ in range(M):
    u, v = map(int, input().split())
    edges[u].append(v)
    edges[v].append(u)

def dfs(edges, v, visited):
    visited[v] = True

    for e in edges[v]:
        if not visited[e]:
            dfs(edges, e, visited)

visited = [False] * (N+1)
cnt = 0
for v in range(1, N+1):
    if not visited[v]:
        dfs(edges, v, visited)
        cnt += 1

print(cnt)