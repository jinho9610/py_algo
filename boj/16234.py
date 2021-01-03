from collections import deque

n, l, r = map(int, input().split())

arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def isInside(x, y):
    return -1 < x < n and -1 < y < n


def findUnions(i, j):
    union = [(i, j)]
    q = deque()
    q.append((i, j))
    c[i][j] = True

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if isInside(nx, ny) and l <= abs(arr[x][y]-arr[nx][ny]) <= r and c[nx][ny] == False:
                q.append((nx, ny))
                c[nx][ny] = True
                union.append((nx, ny))
    unions.append(union)


def moving():
    for union in unions:
        sum = 0
        for i in range(len(union)):
            sum += arr[union[i][0]][union[i][1]]
        avg = sum // len(union)
        for i in range(len(union)):
            arr[union[i][0]][union[i][1]] = avg


cnt = 0
while True:
    unions = []
    c = [[False]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if not c[i][j]:
                findUnions(i, j)
    moving()

    flag = False
    for union in unions:
        if len(union) != 1:
            flag = True

    if flag:
        cnt += 1
    elif not flag and len(unions) == n**2:
        break

print(cnt)
