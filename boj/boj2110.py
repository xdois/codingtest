# 공유기 설치
# 이분탐색
# 정답의 범위 자체를 이분탐색으로 찾자

import sys
input = sys.stdin.readline

n, c = map(int, input().split())
homes = []
for _ in range(n):
    homes.append(int(input()))

homes.sort()
start = 1
end = homes[-1]

ans = 0

while start <= end:
    mid = (start + end) // 2
    curr_home = homes[0] # 첫 좌표에 공유기 설치
    cnt = 1 # 공유기 갯수

    for i in range(n):
        if homes[i] - curr_home >= mid:
            cnt += 1
            curr_home = homes[i]
    
    # 정해진 갯수보다 더 많이 설치했을 경우 더 멀어질 수 있기때문
    if cnt >= c:
        ans = mid
        start = mid + 1
    else:
        end = mid - 1

print(ans)


