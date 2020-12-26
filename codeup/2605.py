# 2605 캔디팡, 정답 맞췄음
arr = []
for _ in range(7):
    arr.append(list(map(int, input().split())))

c = [[False] * 7 for _ in range(7)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def isInside(x, y):
    if 0 <= x < 7 and 0 <= y < 7:
        return True
    else:
        return False


def dfs(x, y, color):
    global cnt
    if c[x][y] == True:
        return False
    else:
        c[x][y] = True  # 방문 처리
        cnt += 1
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if isInside(nx, ny) and c[nx][ny] == False and arr[nx][ny] == color:
                dfs(nx, ny, color)
        return True


result = 0
for i in range(7):
    for j in range(7):
        cnt = 0
        dfs(i, j, arr[i][j])
        if cnt >= 3:
            result += 1

print(result)
