import sys
sys.stdin = open("1206.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    cnt = 0
    
    for i in range(2, N-2):
        left = max(arr[i-1], arr[i-2])
        right = max(arr[i+1], arr[i+2])
        if arr[i] > left and arr[i] > right:
            cnt += arr[i] - max(left, right)
    print(f'#{test_case} {cnt}')
