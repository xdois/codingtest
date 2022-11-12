import sys
input = sys.stdin.readline

n = int(input())

arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

def isSame(x, y, size):
    s = arr[x][y]
    for i in range(size):
        for j in range(size):
            if s != arr[x+i][y+j]:
                return 2
    return s
size = n
countminus = 0
countzero = 0
countplus = 0

def recursion(x, y, size):
    global countplus, countminus, countzero
    k = isSame(x,y,size)
    if k == -1:
        countminus += 1
    elif k == 0:
        countzero += 1
    elif k == 1:
        countplus += 1
    else:
        # 이것도 반복문으로 처리하면 더 깔끔하다 - 피드백
        size = size//3
        x1 = x + size
        y1 = y + size

        x2 = x1 + size
        y2 = y1 + size

        recursion(x,y,size)
        recursion(x,y1,size)
        recursion(x,y2,size)
        recursion(x1,y,size)
        recursion(x1,y1,size)
        recursion(x1,y2,size)
        recursion(x2,y,size)
        recursion(x2,y1,size)
        recursion(x2,y2,size)

recursion(0,0,n)

print(countminus)
print(countzero)
print(countplus)
