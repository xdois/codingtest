import sys
input = sys.stdin.readline

N = int(input())

for _ in range(N):
    stack = []
    # sys.stdin.readline으로 문자열을 입력받으면 뒤에 \n이 붙어있음
    # rstrip으로 공백과 \n 제거 가능
    ps = input().rstrip()
    for i in ps:
        if i == '(':
            stack.append(i)
        else:
            if len(stack) != 0:
                if stack[-1] == '(':
                    stack.pop()
                else:
                    stack.append(i)
            else:
                stack.append(i)
    if len(stack) == 0:
        print('YES')
    else:
        print('NO')

    