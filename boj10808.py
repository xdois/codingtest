s = input()

li = [0] * 26
for i in s:
    li[ord(i) - ord('a')] += 1

print(*li)