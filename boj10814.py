import sys
input = sys.stdin.readline

N = int(input())

li = [list(input().split()) for _ in range(N)]

# 람다를 이용해 나이만 가지고 정렬하도록 함
li.sort(key=lambda x: int(x[0]))

for data in li:
    print(data[0], data[1])