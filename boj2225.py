n,k = map(int, input().split())

dp = []

for _ in range(202):
    li = [0] * 202
    dp.append(li)

for i in range(201):
    dp[1][i] = 1

for i in range(2, k+1):
    for j in range(n+2):
        dp[i][j] = sum(dp[i-1][:j+1])

print(dp[k][n]%int(1e9))

'''
dp[201][201]

dp[i][j] = i개의 수로 j를 만드는 방법
1개의 수로 j를 만드는 방법 = 전부 1
dp[2][j] = dp[1][0] + ... + dp[1][j]

'''