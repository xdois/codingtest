s = input()
a = []
# 소문자,대문자, 나머지
# a~m/n~z 나누기

for c in s:
    if (ord(c) >= 97 and ord(c) <= 109) or (ord(c) >= 65 and ord(c) <= 77):
        a.append(chr(ord(c)+13))
    elif (ord(c) >= 110 and ord(c) <=122) or (ord(c) >= 78 and ord(c) <= 90):
        a.append(chr(ord(c)-13))
    else:
        a.append(c)

print(''.join(a))