######### 시간초과 발생 - 나중에 풀어보기 ##########
'''
import sys
input = sys.stdin.readline

N = int(input())
li = list(map(int, input().split()))
dp = [0] * N

dp[0] = li[0]

# dp[i] = dp[j] + li[j+1] + ... + li[i]가 최대가 되는 값

for i in range(1,N):
    m = li[i]
    for j in range(i):
        d = dp[j]
        for k in range(j+1,i+1):
            d += li[k]
        if d > m:
            m = d
    dp[i] = m

ans = -1000
for i in dp:
    if ans < i:
        ans = i

print(ans)
'''

