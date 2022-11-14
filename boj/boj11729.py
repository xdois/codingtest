# 하노이의 탑 - 재귀

import sys
input = sys.stdin.readline

n = int(input())

def hanoi(n, start, mid, end):
    if n == 1:
        print(start, end)
    else:
        # n-1까지 3을 거쳐서 2로 옮기고
        hanoi(n-1, start, end, mid)
        # 1에서 3으로 가장 큰 원반을 옮기고
        print(start, end)
        # 다시 2로 옮겼던 것들을 1을 거쳐서 3으로 이동
        hanoi(n-1, mid, start, end)

print(2**n-1)
hanoi(n, 1, 2, 3)