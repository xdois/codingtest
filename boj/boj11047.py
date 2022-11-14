import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coin = []
for _ in range(n):
    coin.append(int(input()))
cnt = 0

while k > 0:
    c = coin[-1]
    for i in range(n):
        if coin[i] > k:
            c = coin[i-1]
            break
    #k -= c -> 이렇게 하는 것 보다 아래처럼 몫과 나머지를 활용하면 연산을 줄일 수 있음
    cnt += k // c
    k %= c
        
print(cnt)

