# codeup 4572 영역 나누기
import sys
sys.setrecursionlimit(10**8)

n, m, k = map(int, input().split())

arr = [[0]*m for _ in range(n)]

for _ in range(k):
    a, b, c, d = map(int, input().split())
    for i in range(n):
        for j in range(m):
            if n-d <= i < n-b and a <= j <= c-1:
                arr[i][j] = 1


dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def dfs(x, y):
    global cnt
    if arr[x][y] == 1:
        return False
    else:
        arr[x][y] = 1
        cnt += 1
        for i in range(4):
            nx, ny = x+dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] == 0:
                dfs(nx, ny)
        return True


result = 0
ans = []
for i in range(n):
    for j in range(m):
        cnt = 0
        if arr[i][j] != 1 and dfs(i, j) == True:
            result += 1
            ans.append(cnt)

ans.sort()

print(result)
for i in range(len(ans)):
    print(ans[i], end=' ')
