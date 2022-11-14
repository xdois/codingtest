import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())

for i in range(k):
    if n > 2 * m:
        n -= 1
    else:
        if m > 0:
            m -= 1
        else:
            n -= 1

ans = min(n//2, m)

print(ans)