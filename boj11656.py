input = input()

li = []

for i in range(0,len(input)):
    li.append(input[i:])

li.sort()

for i in li:
    print(i)