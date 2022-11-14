import sys
input = sys.stdin.readline

n = int(input())

arr = []
for _ in range(n):
    arr.append(list(map(int,input().rstrip())))

ans = []
def recursion(x, y, size):
    a = arr[x][y]
    if size == 1:
        ans.append(str(a))
    else:
        isTrue = True
        for i in range(size):
            for j in range(size):
                if arr[x+i][y+j] != a:
                    isTrue = False
                    break
        if not isTrue:
            d = size//2
            ans.append('(')
            recursion(x, y, d)
            recursion(x, y+d, d)
            recursion(x+d, y, d)
            recursion(x+d, y+d, d)
            ans.append(')')
        else:
            ans.append(str(a))

recursion(0,0,n)
print(''.join(ans))
        