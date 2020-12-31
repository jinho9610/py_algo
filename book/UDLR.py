# p.110 #상하좌우 문제
'''
#내 답
def isInside(x, y):
    if 0 < x < n + 1 and 0 < y < n+1:
        return True
    else:
        return False


n = int(input())

arr = [[0] * (n+1) for _ in range(n+1)]

move = input().split()
x = 1
y = 1
for i in range(len(move)):
    if move[i] == 'L':
        if isInside(x, y-1):
            y -= 1
        else:
            continue
    elif move[i] == 'R':
        if isInside(x, y+1):
            y += 1
        else:
            continue
    elif move[i] == 'U':
        if isInside(x-1, y):
            x -= 1
        else:
            continue
    elif move[i] == 'D':
        if isInside(x+1, y):
            x += 1
        else:
            continue

print(str(x)+' '+str(y))
'''

n = int(input())
x, y = 1, 1
plans = input().split()

# L, R, U, D에 따른 이동 방향
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

# 이동 계획 하나씩 확인
for plan in plans:
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue

    x, y = nx, ny

print(x, y)
