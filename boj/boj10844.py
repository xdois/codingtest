n = int(input())

# 각 숫자로 끝나는 계단수가 몇개인지 센다
# 0이나 9로 끝나는경우 -> 다음 자릿수에서 한가지 경우만 가능
# 1~8로 끝나는 경우 -> 다음 자릿수에서 두가지 경우 가능(+-1)

#python 빈 이차원 배열 선언
dp = [[0] * 10 for _ in range(101)]

for i in range(1,10):
    dp[1][i] = 1

for i in range(1, n):
    for j in range(10):
        if j != 0 and j != 9:
            dp[i+1][j-1] += dp[i][j]
            dp[i+1][j+1] += dp[i][j]
        elif j == 0:
            dp[i+1][j+1] += dp[i][j]
        else:
            dp[i+1][j-1] += dp[i][j]

ans = 0
for i in range(10):
    ans += dp[n][i]


# 1e9 -> 부동소수점 표현 -> int 취해줘야함
print(ans%int(1e9))