import sys
input = sys.stdin.readline

N = int(input())

li = []

for _ in range(N):
    (x, y) = map(int, input().split())
    li.append((x,y))

li.sort()

for i in li:
    print(i[0], i[1])