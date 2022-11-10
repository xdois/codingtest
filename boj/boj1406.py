import sys
input = sys.stdin.readline

st = list(input().rstrip('\n'))
current_index = len(st)
N = int(input())

for _ in range(N):
    i = input().split()
    if i[0] == 'L':
        if current_index != 0:
            current_index -= 1
    elif i[0] == 'D':
        if current_index != len(st):
            current_index += 1
    elif i[0] == 'B':
        
        if current_index != 0:
            current_index -= 1
            st.pop(current_index)
    else:
        if current_index == len(st):
            st.append(i[1])
        else:
            st.insert(current_index, i[1])
        current_index += 1

print(''.join(st))