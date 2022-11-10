import sys
input = sys.stdin.readline

N = int(input())
li = list(map(int, input().split()))
dp = [0] * N

dp[0] = 1

for i in range(1, N):
    c = 0
    # 이전 배열을 순회하면서 li[i]를 포함하고 가장 긴 증가하는 부분수열을 찾는다
    for j in range(i):
        if dp[j] > c and li[j] < li[i]:
            c = dp[j]
    dp[i] = c + 1

ans = 0

for i in dp:
    if i > ans:
        ans = i
        
print(ans)
#print(dp)