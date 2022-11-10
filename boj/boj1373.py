s = input().rstrip('\n')
a = list(reversed(list(s)))

while len(a) % 3 != 0:
    a.append('0')

ans = []

for i in range(len(a)//3):
    x = 0
    if a[i*3] == '1':
        x += 1
    if a[i*3+1] == '1':
        x += 2
    if a[i*3+2] == '1':
        x += 4
    
    ans.append(x)
ans.reverse()
print(''.join(map(str, ans)))