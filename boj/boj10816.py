# 10815의 응용
# 미리 각 카드의 갯수를 세둔다
import sys
input = sys.stdin.readline

n = int(input())
cards = list(map(int, input().split()))

cards.sort()

cardDict = {}

m = int(input())
finds = list(map(int, input().split()))

for card in cards:
    if card not in cardDict:
        cardDict[card] = 1
    else:
        cardDict[card] += 1

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
        print(cardDict[cards[ans]], end=' ')
        #print(mid)
print()