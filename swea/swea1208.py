import sys
sys.stdin = open("./input/input1208.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    for i in range(N):
        max_index = arr.index(max(arr))
        min_index = arr.index(min(arr))

        arr[max_index] -= 1
        arr[min_index] += 1

    ans = max(arr) - min(arr)
    print(f'#{test_case} {ans}')