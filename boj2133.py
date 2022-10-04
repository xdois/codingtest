import sys
n = int(input())
dp = [0] * (31)
dp[2] = 3

if n % 2 == 1:
    print(0)
    sys.exit(0)
for i in range(4, n+1):
    if i % 2 == 0:
        #리스트 합계 - sum(list) - 슬라이싱 가능
        # 4,6,8... 칸짜리 모두 두가지씩 추가로 생성 가능
        dp[i] = dp[i-2] * 3 + sum(dp[:i-2]) * 2 + 2
    

print(dp[n])