import sys
input = sys.stdin.readline

n = int(input())
list = []
for _ in range(n):
    a, b = map(int, input().split())
    list.append((a,b))
#print(list)
list.sort()
list_ans = []


for i in range(n):
    temp = [list[i]]
    for j in range(i, n):
        if list[j][0] == temp[-1][0] and list[j][1] < temp[-1][1]:
            temp.pop()
            temp.append(list[j])
        if list[j][0] > temp[-1][1]:
            temp.append(list[j])
    list_ans.append(len(temp))

print(max(list_ans))

