import sys
input = sys.stdin.readline

N = int(input())

# 배열에 숫자들을 append 하는 방식으로 하면 메모리 초과 발생
# 주어지는 수들이 10000 이하이므로 이를 이용한다

l = [0] * 10001

for _ in range(N):
    x = int(input())
    l[x] += 1

for i in range(len(l)):
    # l 전체를 순회하면서 l[i]개만큼 i를 출력
    for j in range(l[i]):
        print(i)