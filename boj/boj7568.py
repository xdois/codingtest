# map - 리스트의 요소를 지정된 함수로 처리
# 배열 출력할때 * 붙이면 [] , 없이 출력 가능

n = int(input())

people = []
for _ in range(n):
    (weight, tall) = map(int, input().split())
    people.append((weight, tall))

#print(people)
answer = []
for i in range(len(people)):
    cnt = 1
    for j in range(len(people)):
        if people[j][0] > people[i][0] and people[j][1] > people[i][1]:
            cnt += 1
    answer.append(cnt)

print(*answer)