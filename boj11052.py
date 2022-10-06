import sys
input = sys.stdin.readline

N = int(input())

card = list(map(int, input().split()))

# 1장 -> card[0] = dp[1]
# 2장 -> max(dp[1]*2, card[1])
# 3장 -> max(dp[1] + dp[2], card[2])
# 4장 -> max(dp[3] + dp[1], dp[2] + dp[2], card[3])
# 5장 -> dp[4] + dp[1] , dp[3] + dp[2] ..
dp = [0] * (N + 1)
dp[1] = card[0]

for i in range(2, N+1):
    price = [card[i-1]]
    for j in range(i):
        price.append(dp[j] + dp[i-j])
    dp[i] = max(price)

print(dp[N])