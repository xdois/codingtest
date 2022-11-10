import sys
input = sys.stdin.readline

N = int(input())

li = []
for _ in range(N):
    li.append(int(input()))

dp = [0] * N

dp[0] = li[0]
if N == 1:
    print(dp[0])
else:
    dp[1] = dp[0] + li[1]
    if N == 2:
        print(dp[1])
    else:
        dp[2] = max(li[0] + li[2], li[1] + li[2])
        if N == 3:
            print(dp[2])
        if N >= 4:
            for i in range(3, N):
                dp[i] = max(dp[i-2], dp[i-3]+li[i-1]) + li[i]

            print(dp[N-1])

# c++ 에서의 return 0 처럼 sys.exit(0)으로 조건문에서 프로그램 중단 가능
# -> 불필요한 조건 제거 가능