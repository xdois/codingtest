import sys
input = sys.stdin.readline

N = int(input())

student = []

for _ in range(N):
    (name, korean, english, math) = input().split()
    student.append((name, korean, english, math))

# 람다에 -(음수기호) 사용 -> 내림차순 가능
student.sort(key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]) )

for s in student:
    print(s[0])