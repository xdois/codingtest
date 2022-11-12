import sys
input = sys.stdin.readline

n = int(input())
li = list(map(int, input().split()))
m = int(input())

li.sort()

start = 0
end = li[-1]
ans = 0
while start <= end:
    mid = (start + end) // 2
    sum = 0

    for l in li:
        if mid > l:
            sum += l
        else:
            sum += mid
    
    if sum <= m:
        ans = mid
        start = mid + 1
    else:
        end = mid - 1

print(ans)