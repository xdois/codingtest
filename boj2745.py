n, b = input().split()
b = int(b)

a = 0
for i in range(len(n)):
    c = n[len(n)-1-i]
    if c.isupper():
        c = ord(c) - 55
    else:
        c = int(c)
    a += c * (b ** i)

print(a)
