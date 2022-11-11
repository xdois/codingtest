import sys

input = sys.stdin.readline

a, p = map(int, input().split())
d = [a]

while True:
    last = d[-1]
    x = 0
    for i in str(last):
        x += (int(i) ** p)

    if x in d:
        print(d.index(x))
        sys.exit(0)
    d.append(x)


