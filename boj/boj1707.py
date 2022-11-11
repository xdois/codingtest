# 이분 그래프
# bfs를 돌면서 색을 칠한다
# 색을 칠할때 인접한 노드에 색이 같은게 있다면 FALSE

import sys
from collections import deque
input = sys.stdin.readline

def bfs(edges, v, visited):
    queue = deque([v])
    visited[v] = 1
    

    while queue:
        now = queue.popleft()

        for e in edges[now]:
            if visited[e] == 0:
                visited[e] = -visited[now]
                queue.append(e)
            else:
                if visited[e] == visited[now]:
                    return False
    return True                


if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        V, E = map(int, input().split())
        edges = [[] for _ in range(V+1)]
        for _ in range(E):
            a, b = map(int, input().split())
            edges[a].append(b)
            edges[b].append(a)

        visited = [0] * (V+1)
        isTrue = True
        for i in range(1, V+1):
            if visited[i] == 0:
                if not bfs(edges, i, visited):
                    isTrue=False
                    break


        print('YES'if isTrue else 'NO')
        