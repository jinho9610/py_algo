n = int(input())

arr = []
for _ in range(n):
    arr.append(list(map(int, list(input()))))

c = [[False]*n for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def isInside(x, y):
    return -1 < x < n and -1 < y < n


def dfs(x, y):
    global cnt
    if c[x][y]:
        return False

    c[x][y] = True
    cnt += 1

    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if isInside(nx, ny) and arr[nx][ny] == 1 and c[nx][ny] == False:
            dfs(nx, ny)
    return True


result = 0
ans = []
for i in range(n):
    for j in range(n):
        cnt = 0
        if arr[i][j] != 0:
            if dfs(i, j):
                result += 1
                ans.append(cnt)

print(result)
ans.sort()
for i in ans:
    print(i)
