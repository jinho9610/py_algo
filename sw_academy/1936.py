# scissor 1      rock 2      paper 3
a, b = map(int, input().split())
if (a == 1 and b == 2) or (a == 2 and b == 3) or (a == 3 and b == 1):
    print('B')
else:
    print('A')
