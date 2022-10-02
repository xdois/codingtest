n = int(input())

dp = [0 for _ in range(n+1)]

dp[1] = 1
# n = 1이면 dp[2] 접근시 오류가 발생하기 때문에 조건 추가
if n >= 2:
    dp[2] = 2

for i in range(3, n+1):
    dp[i] = dp[i-1] + dp[i-2]

print(dp[n]%10007)