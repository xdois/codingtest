import sys
input = sys.stdin.readline
# 몇 줄인지 모르는 입력 대비
while True:
    lower = 0
    upper = 0
    num = 0
    blank = 0
    # 줄바꿈 없애줘야함
    s = input().rstrip('\n')
    if not s:
        break
    for c in s:
        # 쓸 데 없는 짓 하지말고 내장함수 쓰기
        if c.islower():
            lower += 1
        elif c.isupper():
            upper += 1
        elif c.isdigit():
            num += 1
        elif c.isspace():
            blank += 1
    print(lower, upper, num, blank)

