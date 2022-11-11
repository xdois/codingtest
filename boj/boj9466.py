# 각 정점에서 간선이 하나밖에 없는 경우 굳이 인접리스트를 만들지 않아도 됨
# 그래프를 탐색하면서 자신에게 돌아오면 팀 결성
# 자신에게 돌아오지 않으면 팀에 속하지 못함
# 사이클을 저장할 배열을 따로 만들어준다


import sys
input = sys.stdin.readline

sys.setrecursionlimit(10 ** 6)

def dfs(x):
    global result
    visited[x] = True
    cycle.append(x)
    number = arr[x]

    if visited[number]:
        if number in cycle:#사이클이 생기는 경우
            
            result += cycle[cycle.index(number):]
        return
    else:
        dfs(number)
    
        

if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        n = int(input())
        arr = [0] + list(map(int, input().split()))
        visited = [True] + [False] * n
        result = []

        for i in range(1, n+1):
            if not visited[i]:
                cycle = []
                dfs(i)

        print(n - len(result))
        