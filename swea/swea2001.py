import sys
sys.stdin = open("./input/2001.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    arr = []
    for _ in range(N):
        l = list(map(int, input().split()))
        arr.append(l)
    ans = 0

    if N == M:
        ans = sum(arr)
    else:
        
        max = 0
        for i in range(N-M+1):
            for j in range(N-M+1):
                sum = 0
                for a in range(M):
                    for b in range(M):
                        sum += arr[i+a][j+b]

                if sum > max:
                    max = sum
        ans = max
    
    print(f'#{test_case} {ans}')
