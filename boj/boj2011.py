'''
일단 i번째 자릿수가 0이 아니면 dp[i] += dp[i-1]
i-1 i번째 자릿수가 10~26이면 dp[i] += dp[i-2]
마지막에 1000000으로 나눈 나머지
'''
import sys
cipher = input()

dp = [0] * (len(cipher) + 1)

if cipher[0] == '0':
    print(0)
    sys.exit(0)

dp[0] = 1
dp[1] = 1

for i in range(2, len(cipher) + 1):
    if int(cipher[i-1]) > 0:
        dp[i] += dp[i-1]
    num = int(cipher[i-1]) + int(cipher[i-2]) * 10
    if num >= 10 and num <= 26:
        dp[i] += dp[i-2]

print(dp[-1] % 1000000)