n, b = map(int, input().split())
a = []
while n:
    x = n % b
    if x >= 10:
        a.append(chr(x+55))
    else:
        a.append(str(x))
    n = n//b
a = list(reversed(a))
print(''.join(a))