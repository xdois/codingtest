from itertools import combinations
height = []

for _ in range(9):
    height.append(int(input()))

for i in combinations(height, 7):
    sum = 0
    for s in i:
        sum += s
    if sum == 100:
        i = list(i)
        i.sort()
        for ans in i:
            print(ans)
        break

# 9명의 난쟁이중에 7명의 난쟁이를 뽑는 경우의 수 = 9c7 = 9c2 => 작다
# itertools.combinations로 해당하는 모든 list 추출 -> 합을 구함