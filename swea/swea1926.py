#import sys
#sys.stdin = open("input.txt", "r")

N = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for i in range(1, N):
    li = list(map(int, str(i)))
    s = []
    if 3 in li or 6 in li or 9 in li:

        for j in li:
            if j % 3 == 0 and j != 0:
                s.append('-')
        print(''.join(s), end = ' ')
    else:
        print(i, end= ' ')
