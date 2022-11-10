import sys
input = sys.stdin.readline


N = int(input())

que = []

for _ in range(N):
    s = input().split()

    if s[0] == 'push':
        que.append(int(s[1]))
    elif s[0] == 'pop':
        if len(que) == 0:
            print(-1)
        else:
            print(que.pop(0))
    elif s[0] == 'size':
        print(len(que))
    elif s[0] == 'empty':
        if len(que) == 0:
            print(1)
        else:
            print(0)
    elif s[0] == 'front':
        if len(que) == 0:
            print(-1)
        else:
            print(que[0])
    elif s[0] == 'back':
        if len(que) == 0:
            print(-1)
        else:
            print(que[-1])