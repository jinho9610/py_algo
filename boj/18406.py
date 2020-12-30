n = list(input())

digit = len(n)

l, r = 0, 0
for i in range(digit):
    if i < digit/2:
        l += int(n[i])
    else:
        r += int(n[i])

if l == r:
    print('LUCKY')
else:
    print('READY')
