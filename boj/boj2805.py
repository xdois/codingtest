# 나무자르기
# 이분탐색

import sys
input = sys.stdin.readline

n, m = map(int, input().split())

trees = list(map(int, input().split()))

trees.sort()

start = 0
end = max(trees)
cut = 0
#print(f'cut: {cut}')
ans = 0
while start <= end:
    cut = (start + end) // 2
    #print(cut)
    total = 0
    for tree in trees:
        if tree > cut:
            total += tree - cut
    
    if total < m:
        end = cut - 1
    # 자른 결과가 m보다 클 수도 있다
    # 예시: 4 3 / 2 2 2 2
    else:
        ans = cut
        start = cut + 1

print(ans)