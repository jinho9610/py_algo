n, m = map(int, input().split())

arr = []
for _ in range(n):
    arr.append(list(map(int, input())))

# 상하좌우 움직임
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def isInside(x, y):
    if 0 <= x < n and 0 <= y < m:
        return True
    else:
        return False


def dfs(x, y):
    if arr[x][y] == 1:
        return False
    else:
        arr[x][y] = 1
        for i in range(4):
            nx, ny = x + dx[i], y+dy[i]
            if isInside(nx, ny) == True:
                dfs(nx, ny)
        return True


result = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            result += 1

print(result)
