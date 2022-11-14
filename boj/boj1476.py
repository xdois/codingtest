import sys
input = sys.stdin.readline

e, s, m = map(int, input().split())
if e == 15:
    e = 0
if s == 28:
    s = 0
if m == 19:
    m = 0
    
ans = 1
while True:
    if ans % 15 == e and ans % 28 == s and ans % 19 == m:
        break
    ans+=1

print(ans)