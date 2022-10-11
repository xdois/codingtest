import sys
input = sys.stdin.readline

N = int(input())

li = dict()

for _ in range(N):
    key = int(input())
    if key in li:
        li[key] += 1
    else:
        li[key] = 1

max = 0
ans = 0

for key, val in li.items():
    if val > max:
        max = val
        ans = key
    elif val == max:
        ans = min(key, ans)

print(ans)