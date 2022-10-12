import sys
input = sys.stdin.readline

s = input().rstrip()

stack = []

stick = 0
ans = 0
for i in s:
    if i == '(':
        stack.append(1)
        stick += 1
        
    else:
        if stack[-1] == 1:
            stick -= 1
            ans += stick
            
        else:
            ans += 1
            stick -=1
        stack.append(0)

print(ans)

# 만약 ( 일때 - 스택에 (를 쌓는다
# 만약 ()일때 - 앞에 (가 쌓인만큼 더해준다(이때 쌓인거 초기화 x)
# 만약 ()가 아닌 )일때 - 조각 + 1