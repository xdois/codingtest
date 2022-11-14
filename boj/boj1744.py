import sys
input = sys.stdin.readline

n = int(input())
a = []
for _ in range(n):
    a.append(int(input()))
a.sort()
#print(a)
b = [0] * n
b[0] = a[0]
if n > 1:
    b[1] = max(a[0] * a[1], a[0] + a[1])
if n > 2:
    for i in range(2, n):
        b[i] = max(b[i-1] + a[i], b[i-2] + (a[i-1] * a[i]))
    
#print(b)
print(b[n-1])