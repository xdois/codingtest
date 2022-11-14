import sys
from itertools import permutations

input = sys.stdin.readline

n = int(input())
li = list(map(int, input().split()))

def function(arr):
    
    sum = 0
    for i in range(1, n):
        sum += abs(arr[i-1] - arr[i])
    return sum

p = permutations(li, n)
ans = 0
for pp in p:
    ans = max(ans, function(pp))

print(ans)