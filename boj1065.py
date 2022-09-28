# 입력을 그냥 string으로 받으면 자릿수 처리를 편하게 할 수 있다
# 각 자릿수를 int로 변환하고 각 자리가 등차수열을 이루는지 확인

def isArithmetic(str):
    if len(str) <= 2:
        return True
    
    sub = int(str[1]) - int(str[0])

    for i in range(1, len(str)):
        if int(str[i]) - int(str[i-1]) != sub:
            return False
    return True


input = input()

cnt = 0
for i in range(1, int(input)+1):
    if isArithmetic(str(i)):
        cnt += 1

print(cnt)

