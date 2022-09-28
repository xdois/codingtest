def con(str, input):
    c = int(str)
    for i in str:
        c += int(i)
    if c == input:
        return True
    else:
        return False

input = input()
if input == '1':
    print('0')
else:

    for i in range(1, int(input)):
        if con(str(i), int(input)):
            print(i)
            break
        if i == int(input) - 1:
            print('0')

# 더 빠르게 할수있는 방법은 없을까?