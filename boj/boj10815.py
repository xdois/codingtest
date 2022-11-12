import sys
input = sys.stdin.readline

n = int(input())
cards = list(map(int, input().split()))

cards.sort()

m = int(input())
finds = list(map(int, input().split()))

for find in finds:
    start = 0
    end = n-1
    mid = 0
    ans = 0
    while start <= end:
        mid = (start + end) // 2

        if find >= cards[mid]:
            ans = mid
            start = mid + 1
        else:
            end = mid - 1
    
    if cards[ans] != find:
        print(0, end= ' ')
        #print(mid)
    else:
        print(1, end=' ')
        #print(mid)
print()