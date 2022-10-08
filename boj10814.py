import sys
input = sys.stdin.readline

N = int(input())

li = [list(input().split()) for _ in range(N)]

li.sort(key=lambda x: int(x[0]))

for data in li:
    print(data[0], data[1])