# 끝 자리수가 0일때 -> 10가지
# 끝 자리수가 1일때 -> 다음 경우의수 1~9 9가지
# 2일때 -> 8가지
# ...

n = int(input())

dp = [[0] * 10 for _ in range(n+1)]

for i in range(10):
    dp[1][i] = 1

for i in range(2, n+1):
    dp[i][0] = 1
    for j in range(1, 10):
        dp[i][j] = dp[i-1][j] + dp[i][j-1]

ans = 0
for i in range(10):
    ans += dp[n][i]

print(ans%10007)