import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    dp = []
    input_1 = list(map(int, input().split()))
    input_2 = list(map(int, input().split()))
    dp.append(input_1)
    dp.append(input_2)

    max_dp = [[0] * N for _ in range(2)]
    if N == 1:
        print(max(dp[0][0], dp[1][0]))
    else:
        max_dp[0][0] = dp[0][0]
        max_dp[1][0] = dp[1][0]

        max_dp[0][1] = max_dp[1][0] + dp[0][1]
        max_dp[1][1] = max_dp[0][0] + dp[1][1]
        
        if N >= 2:
            for i in range(2, N):
                max_dp[0][i] = max(max_dp[1][i-1], max_dp[0][i-2], max_dp[1][i-2]) + dp[0][i]
                max_dp[1][i] = max(max_dp[0][i-1], max_dp[0][i-2], max_dp[1][i-2]) + dp[1][i]

        
        print(max(max_dp[0][N-1], max_dp[1][N-1]))