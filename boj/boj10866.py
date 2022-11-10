import sys
input = sys.stdin.readline

N = int(input())

deq = []

for _ in range(N):
    s = input().split()

    if s[0] == 'push_front':
        deq.insert(0, int(s[1]))
    elif s[0] == 'push_back':
        deq.append(int(s[1]))
    elif s[0] == 'pop_front':
        if len(deq) == 0:
            print(-1)
        else:
            print(deq.pop(0))
    elif s[0] == 'pop_back':
        if len(deq) == 0:
            print(-1)
        else:
            print(deq.pop())
    elif s[0] == 'size':
        print(len(deq))
    elif s[0] == 'empty':
        if len(deq) == 0:
            print(1)
        else:
            print(0)
    elif s[0] == 'front':
        if len(deq) == 0:
            print(-1)
        else:
            print(deq[0])
    elif s[0] == 'back':
        if len(deq) == 0:
            print(-1)
        else:
            print(deq[-1])