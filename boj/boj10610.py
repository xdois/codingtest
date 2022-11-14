import sys
input = sys.stdin.readline

input = list(map(int, input().rstrip('\n')))
input.sort(reverse=True)

# 마지막 자릿수가 0이 아니라면 절대 불가능
# -> 배열의 마지막 자리가 0이 아니면 불가능
# 나머지 자릿수의 합이 3의 배수라면 가능
# 나머지는 불가능

if input[-1] == 0 and sum(input) % 3 == 0:
    print(''.join(map(str, input)))
else:
    print(-1)