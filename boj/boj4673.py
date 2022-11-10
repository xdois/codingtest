# d(n)을 생성하는 함수
def cons(num):
    result = num
    while num != 0:
        result += num%10
        num = num // 10
    return result

r = []

for i in range(1, 10001):
    r.append(cons(i))
    
for i in range(1, 10001):    
    if i not in r:
        print(i)