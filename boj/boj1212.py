import sys
input = input().rstrip('\n')
a = []

if input == '0':
    print(0)
    sys.exit(0)

for i in input:
    if i == '0':
        a.append('000')
    elif i == '1':
        a.append('001')
    elif i == '2':
        a.append('010')
    elif i == '3':
        a.append('011')
    elif i == '4':
        a.append('100')
    elif i == '5':
        a.append('101')
    elif i == '6':
        a.append('110')
    elif i == '7':
        a.append('111')

print(''.join(a).lstrip('0'))