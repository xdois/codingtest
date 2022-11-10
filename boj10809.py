s = input()

li = [-1] * 26
for i in range(len(s)):
    if li[ord(s[i]) - ord('a')] == -1:
        li[ord(s[i]) - ord('a')] = i

print(*li)