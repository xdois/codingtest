# python3과 pypy3의 속도차이
# input(), sys.stdin.readline() -> 속도 차이
# input = sys.stdin.readline을 코드 처음에 추가하면 됨

import sys
from itertools import permutations
input = sys.stdin.readline


# 숫자의 갯수
n = int(input())

# 숫자 리스트
num_list = list(map(int, input().split()))

op_num = list(map(int, input().split()))
op_list = ['+', '-', '*', '/']
op = []

for k in range(len(op_num)):
    for i in range(op_num[k]):
        op.append(op_list[k])

maximum = -1e9
minimum = 1e9

def solve():
    global maximum, minimum
    o = permutations(op, n-1)
    #같은 연산자가 여러개인경우 중복이 생김
    # set을 통해 중복을 제거하여 시간, 메모리 절약
    o = list(set(o))
    for case in o:
        total = num_list[0]
        for r in range(1, n):
            if case[r-1] == '+':
                total += num_list[r]
            elif case[r-1] == '-':
                total -= num_list[r]
            elif case[r-1] == '*':
                total *= num_list[r]
            elif case[r-1] == '/':
                total = int(total/num_list[r])

        if total > maximum:
            maximum = total
            
        if total < minimum:
            minimum = total
            

solve()
print(maximum)
print(minimum)
