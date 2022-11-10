import sys
sys.stdin = open("./input/input1204.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    arr_max = [0] * 101
    for i in arr:
        arr_max[i] += 1
    ans = 0
    x = 0
    for i in range(len(arr_max)):
        if x <= arr_max[i]:
            ans = i
            x = arr_max[i]

    print(f'#{N} {ans}')